# -*- coding: utf-8 -*-
"""
SWAPI ETL - Star Wars Characters Data Extraction and Analysis

This script extracts data from the Star Wars API (SWAPI), transforms it,
and exports it in both CSV and JSON formats for analysis.
"""

import pandas as pd
from src.config import CATEGORIES
from src.api_client import get_all_swapi_data
from src.transformers import transform_people_dataframe
from src.exporters import save_dataframe_as_csv, export_swapi_category


def main():
    """Main ETL pipeline for SWAPI data."""
    
    print("Starting SWAPI ETL process...")
    
    # Step 1: Extract film data and release dates
    print("\n1. Extracting film data...")
    films_data = get_all_swapi_data('films')
    films_release_dates = {
        film['title']: int(film['release_date'][:4]) 
        for film in films_data
    }
    print(f"   Found {len(films_data)} films")
    
    # Step 2: Extract and transform people data
    print("\n2. Extracting and transforming people data...")
    people_data = get_all_swapi_data('people')
    print(f"   Found {len(people_data)} characters")
    
    people_dataframe = pd.DataFrame(people_data)
    
    print("   Transforming data (this may take a few minutes)...")
    people_dataframe = transform_people_dataframe(people_dataframe, films_release_dates)
    
    # Step 3: Save people data
    print("\n3. Saving people dataset...")
    save_dataframe_as_csv(people_dataframe, 'swapi_people_dataset.csv')
    
    # Step 4: Export all categories
    print("\n4. Exporting all SWAPI categories...")
    for category in CATEGORIES.keys():
        print(f"   Processing {category}...")
        category_data = get_all_swapi_data(category)
        export_swapi_category(category, category_data)
    
    print("\n✓ ETL process completed successfully!")
    print("All data has been saved to the 'data' directory.")


if __name__ == "__main__":
    main()
