# -*- coding: utf-8 -*-
"""Configuration constants for the SWAPI ETL project."""

# SWAPI API Configuration
SWAPI_ENDPOINT = 'https://swapi.py4e.com/api/'

# Available SWAPI Categories
CATEGORIES = {
    'films': f"{SWAPI_ENDPOINT}/films/",
    'people': f"{SWAPI_ENDPOINT}/people/",
    'planets': f"{SWAPI_ENDPOINT}/planets/",
    'species': f"{SWAPI_ENDPOINT}/species/",
    'starships': f"{SWAPI_ENDPOINT}/starships/",
    'vehicles': f"{SWAPI_ENDPOINT}/vehicles/"
}

# Weight Segmentation Ranges (in kg)
WEIGHT_SEGMENTS = [
    (15, 35, '15-35 kg'),
    (36, 70, '36-70 kg'),
    (71, 80, '71-80 kg'),
    (81, 100, '81-100 kg'),
    (101, 140, '101-140 kg'),
    (141, float('inf'), '141+ kg')
]
