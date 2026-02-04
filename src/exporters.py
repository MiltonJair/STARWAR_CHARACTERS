# -*- coding: utf-8 -*-
"""Data export functions for saving processed data."""

import json
import pandas as pd
from typing import List, Dict, Any
from pathlib import Path


def save_dataframe_as_csv(dataframe: pd.DataFrame, filename: str, output_dir: str = 'data') -> None:
    """
    Save a pandas DataFrame as a CSV file.
    
    Args:
        dataframe: The DataFrame to save
        filename: Name of the output file (without path)
        output_dir: Directory to save the file (default: 'data')
    """
    output_path = Path(output_dir) / filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")


def save_data_as_json(data: List[Dict[str, Any]], filename: str, output_dir: str = 'data') -> None:
    """
    Save data as a JSON file.
    
    Args:
        data: The data to save (list of dictionaries)
        filename: Name of the output file (without path)
        output_dir: Directory to save the file (default: 'data')
    """
    output_path = Path(output_dir) / filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {output_path}")


def export_swapi_category(category: str, data: List[Dict[str, Any]], output_dir: str = 'data') -> None:
    """
    Export SWAPI category data as both CSV and JSON.
    
    Args:
        category: Name of the category (e.g., 'people', 'films')
        data: The data to export
        output_dir: Directory to save the files (default: 'data')
    """
    # Save as CSV
    dataframe = pd.DataFrame(data)
    save_dataframe_as_csv(dataframe, f'swapi_{category}.csv', output_dir)
    
    # Save as JSON
    save_data_as_json(data, f'swapi_{category}.json', output_dir)
