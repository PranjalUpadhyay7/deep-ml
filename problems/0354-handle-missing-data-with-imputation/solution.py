import numpy as np
import pandas as pd

def impute_missing_data(data: np.ndarray, strategy: str = 'mean') -> np.ndarray:
    """
    Impute missing values in a 2D array using the specified strategy.
    
    Args:
        data: 2D numpy array with missing values represented as np.nan
        strategy: Imputation strategy - 'mean', 'median', or 'mode'
        
    Returns:
        2D numpy array with missing values imputed
    """
    
    df = pd.DataFrame(data)
    
    if strategy == 'mean':
        fill_values = df.mean(axis=0)
    elif strategy == 'median':
        fill_values = df.median(axis=0)
    elif strategy == 'mode':
        # .mode() returns a DataFrame (since there can be multiple modes). 
        # .iloc[0] grabs the first mode for each column.
        fill_values = df.mode(axis=0).iloc[0]
    
    return df.fillna(fill_values).to_numpy()
