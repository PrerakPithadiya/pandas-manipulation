import pandas as pd


def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing values in the 'quantity' column of the products DataFrame.

    This function takes a DataFrame containing product information and fills
    any missing values in the 'quantity' column with 0. This ensures that all
    products have a valid quantity value for further processing or analysis.

    Parameters:
    -----------
    products : pd.DataFrame
        A DataFrame containing product information. It must have a 'quantity' column.

    Returns:
    --------
    pd.DataFrame
        A new DataFrame with the same structure as the input, but with missing
        values in the 'quantity' column filled with 0.

    Example:
    --------
    >>> import pandas as pd
    >>> data = {'product': ['A', 'B', 'C'], 'quantity': [1, None, 3]}
    >>> df = pd.DataFrame(data)
    >>> filled_df = fillMissingValues(df)
    >>> print(filled_df)
      product  quantity
    0       A       1.0
    1       B       0.0
    2       C       3.0

    Note:
    -----
    This function assumes that the input DataFrame has a 'quantity' column.
    If the column doesn't exist, a KeyError will be raised.
    """
    # Fill missing values in the quantity column with 0
    products["quantity"] = products["quantity"].fillna(0)

    # Return the updated DataFrame
    return products
