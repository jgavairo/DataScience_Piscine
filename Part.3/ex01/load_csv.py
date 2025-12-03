import pandas as pandas


def load(path: str) -> pandas.DataFrame:
    """Load a CSV file into a pandas DataFrame.

    Args:
        path (str): The path to the CSV file.

    Returns:
        pandas.DataFrame if successful, None otherwise.
    """
    try:
        data = pandas.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except Exception:
        return None

