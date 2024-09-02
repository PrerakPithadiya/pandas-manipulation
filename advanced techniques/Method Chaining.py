import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    """
    Find and return heavy animals from the given DataFrame.

    This function filters animals with a weight greater than 100 units,
    sorts them in descending order of weight, and returns their names.

    Parameters:
    -----------
    animals : pd.DataFrame
        A DataFrame containing animal data. It should have at least
        two columns: 'weight' (numeric) and 'name' (string).

    Returns:
    --------
    pd.DataFrame
        A DataFrame containing only the 'name' column of heavy animals
        (weight > 100), sorted in descending order of weight.

    Example:
    --------
    >>> import pandas as pd
    >>> data = {'name': ['Lion', 'Elephant', 'Tiger', 'Bear'],
    ...         'weight': [190, 4000, 200, 300]}
    >>> df = pd.DataFrame(data)
    >>> result = findHeavyAnimals(df)
    >>> print(result)
       name
    1  Elephant
    3  Bear
    2  Tiger
    0  Lion
    """
    return animals[animals["weight"] > 100].sort_values(by="weight", ascending=False)[
        ["name"]
    ]
