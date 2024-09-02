import pandas as pd


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Modifies the salary column of the input DataFrame by doubling each salary.

    This function takes a DataFrame containing employee information and modifies
    the 'salary' column by multiplying each salary by 2. The original DataFrame
    is modified in-place, and the updated DataFrame is returned.

    Parameters:
    -----------
    employees : pd.DataFrame
        A DataFrame containing employee information. It must have a 'salary' column.

    Returns:
    --------
    pd.DataFrame
        The modified DataFrame with updated salary values.

    Notes:
    ------
    - This function assumes that the 'salary' column exists in the input DataFrame.
    - The function modifies the original DataFrame in-place.
    - Make sure the 'salary' column contains numeric values for proper multiplication.

    Example:
    --------
    >>> import pandas as pd
    >>> data = {'name': ['Alice', 'Bob', 'Charlie'], 'salary': [50000, 60000, 70000]}
    >>> df = pd.DataFrame(data)
    >>> modified_df = modifySalaryColumn(df)
    >>> print(modified_df)
    """
    # Modify the salary column by multiplying each salary by 2
    employees["salary"] = employees["salary"] * 2

    # Return the updated DataFrame
    return employees
