import pandas as pd


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    """
    Change the data type of the 'grade' column in the students DataFrame.

    This function takes a DataFrame containing student information and converts
    the 'grade' column from float to integer data type. This conversion is useful
    for ensuring consistency in grade representation and for potential
    downstream analysis that requires integer grades.

    Parameters:
    -----------
    students : pd.DataFrame
        A DataFrame containing student information. It must include a 'grade' column.

    Returns:
    --------
    pd.DataFrame
        A DataFrame with the same structure as the input, but with the 'grade'
        column converted to integer type.

    Notes:
    ------
    - This function assumes that the 'grade' column exists in the input DataFrame.
    - Any decimal values in the 'grade' column will be truncated, not rounded.
    - NaN values, if present, will be converted to NaN in integer type.

    Example:
    --------
    >>> import pandas as pd
    >>> data = {'name': ['Alice', 'Bob', 'Charlie'], 'grade': [85.5, 90.0, 78.3]}
    >>> df = pd.DataFrame(data)
    >>> result = changeDatatype(df)
    >>> print(result.dtypes)
    name     object
    grade     int64
    dtype: object
    """
    # Convert the grade column from float to int
    students["grade"] = students["grade"].astype(int)

    # Return the updated DataFrame
    return students
