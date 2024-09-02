import pandas as pd


def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    """
    Reshape a DataFrame from wide to long format using the melt operation.

    This function takes a DataFrame with product sales data in a wide format
    (where each quarter is a separate column) and converts it to a long format
    (where quarter becomes a variable and sales are in a single column).

    Parameters:
    -----------
    report : pd.DataFrame
        The input DataFrame in wide format. It should have a 'product' column
        and multiple columns for different quarters.

    Returns:
    --------
    pd.DataFrame
        A reshaped DataFrame in long format with columns:
        - 'product': The product identifier
        - 'quarter': The quarter (previously column names)
        - 'sales': The sales values

    Example:
    --------
    >>> import pandas as pd
    >>> data = pd.DataFrame({
    ...     'product': ['A', 'B', 'C'],
    ...     'Q1': [100, 200, 300],
    ...     'Q2': [150, 250, 350]
    ... })
    >>> melted = meltTable(data)
    >>> print(melted)
      product quarter  sales
    0      A      Q1    100
    1      B      Q1    200
    2      C      Q1    300
    3      A      Q2    150
    4      B      Q2    250
    5      C      Q2    350

    Notes:
    ------
    - The function assumes that the input DataFrame has a 'product' column
      and that all other columns (except 'product') represent quarters.
    - The resulting DataFrame will have the same number of rows as the
      input DataFrame multiplied by the number of quarter columns.
    """
    # Melt the DataFrame
    melted = pd.melt(
        report, id_vars=["product"], var_name="quarter", value_name="sales"
    )

    # Return the reshaped DataFrame
    return melted
