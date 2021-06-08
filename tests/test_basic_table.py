import pandas as pd

import sharptable


def _sample_pandas_df() -> pd.DataFrame:
    """
    Sample DataFrame for basic testing and experimentation.

    Returns:

    """

    df = pd.DataFrame([{"a": 1, "b": 2}, {"a": 3, "b": 4}])
    return df


def test_basic_table_visualization() -> None:
    """
    Basic plotting test.
    """

    df = _sample_pandas_df()

    ds = sharptable.datastores.PandasDatastore(df)
    table = sharptable.tables.MatplotlibTable(ds)

    table.show()


def test_basic_table_save() -> None:
    """
    """

    df = _sample_pandas_df()

    ds = sharptable.datastores.PandasDatastore(df)
    table = sharptable.tables.MatplotlibTable(ds)

    table.savefig("temp")
