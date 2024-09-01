import pandas as pd


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Select the first three rows of a DataFrame.

    This function takes a pandas DataFrame as input and returns a new DataFrame
    containing only the first three rows of the original DataFrame.

    Args:
        employees (pd.DataFrame): The input DataFrame containing employee data.

    Returns:
        pd.DataFrame: A new DataFrame with the first three rows of the input DataFrame.

    Example:
        >>> import pandas as pd
        >>> data = pd.DataFrame({'Name': ['John', 'Jane', 'Bob', 'Alice'],
        ...                      'Age': [30, 25, 35, 28]})
        >>> result = selectFirstRows(data)
        >>> print(result)
           Name  Age
        0  John   30
        1  Jane   25
        2   Bob   35
    """
    # Select the first 3 rows of the DataFrame
    result = employees.head(3)

    # Return the selected rows
    return result
