import pandas as pd
from typing import List


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    """
    Create a DataFrame from a 2D list of student data.

    This function takes a 2D list containing student information and converts it
    into a pandas DataFrame. Each inner list in the input should contain two
    integer values: the student ID and the student's age.

    Parameters:
    -----------
    student_data : List[List[int]]
        A 2D list where each inner list contains two integers:
        [student_id, age]

    Returns:
    --------
    pd.DataFrame
        A pandas DataFrame with two columns: 'student_id' and 'age'

    Example:
    --------
    >>> data = [[1, 15], [2, 16], [3, 17]]
    >>> df = createDataframe(data)
    >>> print(df)
       student_id  age
    0           1   15
    1           2   16
    2           3   17

    Notes:
    ------
    - Ensure that the input list contains valid integer values for both
      student ID and age.
    - The function assumes that the input data is correctly formatted and
      does not perform extensive error checking.
    """
    # Create a DataFrame from the 2D list
    df = pd.DataFrame(student_data, columns=["student_id", "age"])
    return df
