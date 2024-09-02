import pandas as pd


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    """
    Remove rows with missing values in the 'name' column from the given DataFrame.

    This function takes a DataFrame containing student information and removes any rows
    where the 'name' column has missing values. It helps to clean the data by ensuring
    that all remaining records have a valid name.

    Parameters:
    -----------
    students : pd.DataFrame
        The input DataFrame containing student information.

    Returns:
    --------
    pd.DataFrame
        A new DataFrame with rows containing missing names removed.

    Example:
    --------
    >>> import pandas as pd
    >>> data = pd.DataFrame({'name': ['John', None, 'Alice'], 'age': [25, 30, 22]})
    >>> cleaned_data = dropMissingData(data)
    >>> print(cleaned_data)
       name  age
    0  John   25
    2 Alice   22
    """
    # Remove rows where there are missing values in the 'name' column
    students = students.dropna(subset=["name"])

    # Return the updated DataFrame
    return students
