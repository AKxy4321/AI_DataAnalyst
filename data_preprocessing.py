
#################################################################################
############## Data Processing Module ###########################################
#################################################################################

from scipy import stats
import pandas as pd
import numpy as np
import json


def load_data(file_path: str) -> pd.DataFrame:
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.json'):
        return pd.read_json(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format")


def clean_data(file_path: str, normalise: bool = False) -> pd.DataFrame:

    df = load_data(file_path=file_path)
    # Fill missing values in numeric columns with the mean of each column

    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_cols:
        df[col].fillna(df[col].mean(), inplace=True)
    
    # Drop Duplicates
    
    df.drop_duplicates(inplace=True)

    if normalise:
        # Normalize numeric columns

        for col in numeric_cols:
            min_val = df[col].min()
            max_val = df[col].max()
            df[col] = (df[col] - min_val) / (max_val - min_val)

    # Fill missing values in string columns with the mode of each column

    string_cols = df.select_dtypes(include=['object']).columns
    for col in string_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)  

    return df