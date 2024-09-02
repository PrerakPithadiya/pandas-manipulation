import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    """
    Create a pivot table from a weather DataFrame.

    This function takes a DataFrame containing weather data and creates a pivot table
    that reorganizes the data based on specified parameters.

    Parameters:
    -----------
    weather : pd.DataFrame
        Input DataFrame containing weather data. It should have columns for 'month',
        'city', and 'temperature'.

    Returns:
    --------
    pd.DataFrame
        A pivot table with months as the index, cities as columns, and temperature
        values in the cells.

    Notes:
    ------
    - The input DataFrame should have at least three columns: 'month', 'city', and 'temperature'.
    - The function uses pandas' pivot() method to reshape the data.
    - Missing values in the resulting pivot table will be filled with NaN.

    Example:
    --------
    >>> import pandas as pd
    >>> data = {'month': ['Jan', 'Jan', 'Feb', 'Feb'],
    ...         'city': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
    ...         'temperature': [0, 15, 2, 17]}
    >>> df = pd.DataFrame(data)
    >>> result = pivotTable(df)
    >>> print(result)
    city      Los Angeles  New York
    month
    Feb              17.0       2.0
    Jan              15.0       0.0
    """
    df = weather.pivot(index="month", columns="city", values="temperature")

    return df
