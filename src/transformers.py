# -*- coding: utf-8 -*-
"""Data transformation functions for SWAPI data."""

import pandas as pd
from typing import List, Union
from .config import WEIGHT_SEGMENTS
from .api_client import get_resource_name, get_resource_names


def calculate_age(birth_year: str, release_dates: List[int]) -> Union[int, str]:
    """
    Calculate the age of a character at the time of the first film.
    
    Args:
        birth_year: The birth year of the character (e.g., '19BBY' or 'unknown')
        release_dates: List of film release dates
        
    Returns:
        The calculated age or the original birth_year if calculation is not possible
    """
    if birth_year == 'unknown':
        return 'unknown'

    try:
        numeric_birth_year = int(birth_year)
    except ValueError:
        # Handle special cases like '19BBY'
        return birth_year

    for release_date in release_dates:
        if numeric_birth_year <= release_date:
            return release_date - numeric_birth_year
    return release_dates[-1] - numeric_birth_year


def segment_gender(gender: str) -> str:
    """
    Segment gender into standardized categories.
    
    Args:
        gender: The gender value
        
    Returns:
        Standardized gender segment
    """
    if gender == 'female':
        return 'Female'
    elif gender == 'male':
        return 'Male'
    elif gender == 'hermaphrodite':
        return 'Hermaphrodite'
    else:
        return 'N/A'


def segment_weight(weight: Union[float, str]) -> str:
    """
    Segment weight into predefined ranges.
    
    Args:
        weight: The weight value in kg
        
    Returns:
        Weight segment label
    """
    if weight == 'unknown' or pd.isna(weight):
        return 'Unknown'
    
    weight = float(weight)
    
    for min_weight, max_weight, label in WEIGHT_SEGMENTS:
        if min_weight <= weight <= max_weight:
            return label
    
    return 'Unknown'


def transform_people_dataframe(people_df: pd.DataFrame, films_release_dates: dict) -> pd.DataFrame:
    """
    Transform the people dataframe with additional calculated fields.
    
    Args:
        people_df: Raw people dataframe from SWAPI
        films_release_dates: Dictionary mapping film titles to release years
        
    Returns:
        Transformed dataframe with additional columns
    """
    # Calculate age at first film
    people_df['age_at_first_film'] = people_df.apply(
        lambda row: calculate_age(row['birth_year'], list(films_release_dates.values())), 
        axis=1
    )
    
    # Convert homeworld URLs to names
    people_df['homeworld'] = people_df['homeworld'].apply(get_resource_name)
    
    # Convert species URLs to names
    people_df['species'] = people_df['species'].apply(get_resource_names)
    
    # Convert vehicle URLs to names
    people_df['vehicles'] = people_df['vehicles'].apply(get_resource_names)
    
    # Convert starship URLs to names
    people_df['starships'] = people_df['starships'].apply(get_resource_names)
    
    # Convert film URLs to titles
    people_df['films'] = people_df['films'].apply(lambda urls: get_resource_names(urls, 'title'))
    
    # Add gender segmentation
    people_df['gender_segment'] = people_df['gender'].apply(segment_gender)
    
    # Convert mass to numeric and add weight segmentation
    people_df['mass_numeric'] = pd.to_numeric(people_df['mass'], errors='coerce')
    people_df['weight_segment'] = people_df['mass_numeric'].apply(segment_weight)
    
    # Calculate derived metrics
    people_df['num_films'] = people_df['films'].apply(len)
    people_df['num_vehicles'] = people_df['vehicles'].apply(len)
    people_df['num_species'] = people_df['species'].apply(lambda x: len(set(x)))
    
    return people_df
