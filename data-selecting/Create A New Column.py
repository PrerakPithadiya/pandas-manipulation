import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Create a new 'bonus' column in the employees DataFrame.

    This function takes an input DataFrame containing employee information
    and adds a new column 'bonus' with values that are double the 'salary' column.

    Parameters:
    -----------
    employees : pd.DataFrame
        Input DataFrame containing employee information.
        It must have a 'salary' column.

    Returns:
    --------
    pd.DataFrame
        Updated DataFrame with the new 'bonus' column added.

    Example:
    --------
    >>> import pandas as pd
    >>> data = {'name': ['John', 'Jane'], 'salary': [50000, 60000]}
    >>> df = pd.DataFrame(data)
    >>> result = createBonusColumn(df)
    >>> print(result)
       name  salary   bonus
    0  John   50000  100000
    1  Jane   60000  120000

    Notes:
    ------
    - The function assumes that the 'salary' column exists in the input DataFrame.
    - The 'bonus' column is calculated as twice the value of the 'salary' column.
    - The original DataFrame is modified in-place and also returned.

    Raises:
    -------
    KeyError
        If the 'salary' column is not present in the input DataFrame.
    """
    # Create a new column 'bonus' with doubled values of the 'salary' column
    employees["bonus"] = employees["salary"] * 2

    # Return the updated DataFrame
    return employees
