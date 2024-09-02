"""
Table Reshaping - Concatenate

This module provides functionality to concatenate two pandas DataFrames vertically.

Functions:
    concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        Concatenates two DataFrames vertically.

Usage:
    This script can be run as a standalone program to test the concatenateTables function
    with various test cases.

Dependencies:
    - pandas

Author: [Your Name]
Date: [Current Date]
Version: 1.0
"""

import pandas as pd


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    Concatenates two pandas DataFrames vertically.

    Args:
        df1 (pd.DataFrame): The first DataFrame to concatenate.
        df2 (pd.DataFrame): The second DataFrame to concatenate.

    Returns:
        pd.DataFrame: A new DataFrame containing the rows from both input DataFrames.

    Note:
        - The function uses pd.concat with axis=0 to perform vertical concatenation.
        - The resulting DataFrame will have a reset index.
    """
    result = pd.concat([df1, df2], axis=0, ignore_index=True)
    return result


if __name__ == "__main__":
    # Test case 1: Basic concatenation with matching columns
    df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})
    result = concatenateTables(df1, df2)
    print("Test case 1: Basic concatenation with matching columns")
    print(result)
    print()

    # Test case 2: Concatenation with different columns
    df3 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    df4 = pd.DataFrame({"B": [5, 6], "C": [7, 8]})
    result = concatenateTables(df3, df4)
    print("Test case 2: Concatenation with different columns")
    print(result)
    print()

    # Test case 3: Concatenation with an empty DataFrame
    df5 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    df6 = pd.DataFrame()
    result = concatenateTables(df5, df6)
    print("Test case 3: Concatenation with an empty DataFrame")
    print(result)
    print()

    # Test case 4: Concatenation with mixed data types
    df7 = pd.DataFrame({"A": [1, 2], "B": ["a", "b"]})
    df8 = pd.DataFrame({"A": [3.0, 4.0], "B": [True, False]})
    result = concatenateTables(df7, df8)
    print("Test case 4: Concatenation with mixed data types")
    print(result)
    print()
