import logging

import pandas as pd

import sharptable

log = logging.getLogger()


def sample_pandas_df() -> pd.DataFrame:
    """
    Sample DataFrame for basic testing and experimentation.

    Returns:

    """

    df = pd.DataFrame([{"a": 1, "b": 2}, {"a": 3, "b": 4}])
    return df


def test_basic_table_visualization() -> None:
    """
    Basic plotting t
    """

    df = sample_pandas_df()

    ds = sharptable.datastores.PandasDatastore(df)
    table = sharptable.tables.MatplotlibTable(ds)

    table.show()
