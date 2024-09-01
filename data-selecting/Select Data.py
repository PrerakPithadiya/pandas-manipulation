import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    """
    Selects specific data from a DataFrame of student information.

    This function filters the input DataFrame to return only the rows where
    the student_id is 101, and selects only the 'name' and 'age' columns.

    Parameters:
    -----------
    students : pd.DataFrame
        A DataFrame containing student information. It should have at least
        the following columns: 'student_id', 'name', and 'age'.

    Returns:
    --------
    pd.DataFrame
        A new DataFrame containing only the 'name' and 'age' columns for
        students with student_id 101.

    Example:
    --------
    >>> import pandas as pd
    >>> data = {'student_id': [101, 102, 101, 103],
    ...         'name': ['Alice', 'Bob', 'Charlie', 'David'],
    ...         'age': [20, 22, 21, 23],
    ...         'grade': [85, 92, 88, 95]}
    >>> df = pd.DataFrame(data)
    >>> result = selectData(df)
    >>> print(result)
         name  age
    0   Alice   20
    2  Charlie  21
    """
    # Select the rows where student_id is 101 and only the 'name' and 'age' columns
    result = students.loc[students["student_id"] == 101, ["name", "age"]]

    # Return the result
    return result
