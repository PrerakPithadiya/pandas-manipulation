import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows from a DataFrame based on the 'email' column.

    This function takes a DataFrame containing customer information and removes
    duplicate entries based on the 'email' column. It keeps only the first occurrence
    of each unique email address.

    Parameters:
    -----------
    customers : pd.DataFrame
        The input DataFrame containing customer information. It must have an 'email' column.

    Returns:
    --------
    pd.DataFrame
        A new DataFrame with duplicate rows removed, keeping only the first occurrence
        of each unique email address.

    Notes:
    ------
    - This function assumes that the input DataFrame has an 'email' column.
    - The original DataFrame is not modified; a new DataFrame is returned instead.
    - If there are no duplicate emails, the returned DataFrame will be identical to the input.
    - The function uses the `drop_duplicates` method from pandas with `subset="email"` and `keep="first"`.

    Example:
    --------
    >>> import pandas as pd
    >>> data = {'name': ['John', 'Jane', 'John'], 'email': ['john@example.com', 'jane@example.com', 'john@example.com']}
    >>> df = pd.DataFrame(data)
    >>> result = dropDuplicateEmails(df)
    >>> print(result)
       name              email
    0  John  john@example.com
    1  Jane  jane@example.com

    See Also:
    ---------
    pandas.DataFrame.drop_duplicates : The underlying pandas method used for removing duplicates.

    Version:
    --------
    1.0.0

    Author:
    -------
    [Your Name or Organization]

    License:
    --------
    [License Information, e.g., MIT License]

    Project Repository:
    -------------------
    [Link to the project repository, if applicable]

    Dependencies:
    -------------
    - pandas (>=1.0.0)

    Changelog:
    ----------
    - 1.0.0 (YYYY-MM-DD): Initial release
    """
    # Remove duplicate rows based on the 'email' column, keeping only the first occurrence
    customers = customers.drop_duplicates(subset="email", keep="first")

    # Return the updated DataFrame
    return customers


# Test cases
if __name__ == "__main__":
    """
    Test suite for the dropDuplicateEmails function.

    This section contains various test cases to verify the functionality of the
    dropDuplicateEmails function under different scenarios.

    Test Cases:
    -----------
    1. DataFrame with duplicate emails
    2. DataFrame without duplicate emails
    3. Empty DataFrame
    4. DataFrame with all duplicate emails

    Each test case prints its result for visual inspection.

    Note: These test cases are not exhaustive and are meant for basic functionality checking.
    For a more robust testing approach, consider using a testing framework like pytest.
    """

    # Test case 1: DataFrame with duplicate emails
    data1 = {
        "name": ["John", "Jane", "John", "Alice"],
        "email": [
            "john@example.com",
            "jane@example.com",
            "john@example.com",
            "alice@example.com",
        ],
    }
    df1 = pd.DataFrame(data1)
    result1 = dropDuplicateEmails(df1)
    print("Test case 1 result:")
    print(result1)
    print()

    # Test case 2: DataFrame without duplicate emails
    data2 = {
        "name": ["John", "Jane", "Alice"],
        "email": ["john@example.com", "jane@example.com", "alice@example.com"],
    }
    df2 = pd.DataFrame(data2)
    result2 = dropDuplicateEmails(df2)
    print("Test case 2 result:")
    print(result2)
    print()

    # Test case 3: Empty DataFrame
    df3 = pd.DataFrame(columns=["name", "email"])
    result3 = dropDuplicateEmails(df3)
    print("Test case 3 result:")
    print(result3)
    print()

    # Test case 4: DataFrame with all duplicate emails
    data4 = {
        "name": ["John", "Jane", "Alice", "Bob"],
        "email": [
            "same@example.com",
            "same@example.com",
            "same@example.com",
            "same@example.com",
        ],
    }
    df4 = pd.DataFrame(data4)
    result4 = dropDuplicateEmails(df4)
    print("Test case 4 result:")
    print(result4)
