# -*- coding: utf-8 -*-
"""API client for interacting with SWAPI (Star Wars API)."""

import requests
from typing import List, Dict, Any
from .config import CATEGORIES


def get_all_swapi_data(category: str) -> List[Dict[str, Any]]:
    """
    Fetch all data from SWAPI for a given category.
    
    Args:
        category: The category to fetch (e.g., 'people', 'films', 'planets')
        
    Returns:
        List of dictionaries containing the data
    """
    all_data = []
    next_page = CATEGORIES[category]

    while next_page:
        response = requests.get(next_page)
        response.raise_for_status()  # Raise exception for bad status codes
        data = response.json()
        all_data.extend(data['results'])
        next_page = data['next']

    return all_data


def get_resource_name(url: str, name_key: str = 'name') -> str:
    """
    Fetch a resource from SWAPI and return its name.
    
    Args:
        url: The URL of the resource
        name_key: The key to extract from the response (default: 'name')
        
    Returns:
        The name of the resource
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for bad status codes
    data = response.json()
    return data.get(name_key, 'Unknown')


def get_resource_names(urls: List[str], name_key: str = 'name') -> List[str]:
    """
    Fetch multiple resources from SWAPI and return their names.
    
    Args:
        urls: List of resource URLs
        name_key: The key to extract from the response (default: 'name')
        
    Returns:
        List of resource names
    """
    names = []
    for url in urls:
        names.append(get_resource_name(url, name_key))
    return names
