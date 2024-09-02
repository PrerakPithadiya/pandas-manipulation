import pandas as pd


def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    """
    Rename columns of the input DataFrame according to specified mappings.

    This function takes a DataFrame containing student information and renames
    its columns to more descriptive names. The renaming is done as follows:
    - 'id' becomes 'student_id'
    - 'first' becomes 'first_name'
    - 'last' becomes 'last_name'
    - 'age' becomes 'age_in_years'

    Parameters:
    -----------
    students : pd.DataFrame
        Input DataFrame containing student information with original column names.

    Returns:
    --------
    pd.DataFrame
        A new DataFrame with renamed columns, preserving the original data.

    Example:
    --------
    >>> import pandas as pd
    >>> data = {'id': [1, 2], 'first': ['John', 'Jane'], 'last': ['Doe', 'Smith'], 'age': [20, 22]}
    >>> df = pd.DataFrame(data)
    >>> renamed_df = renameColumns(df)
    >>> print(renamed_df.columns)
    Index(['student_id', 'first_name', 'last_name', 'age_in_years'], dtype='object')
    """
    # Rename the columns as specified
    students = students.rename(
        columns={
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years",
        }
    )

    # Return the updated DataFrame
    return students
