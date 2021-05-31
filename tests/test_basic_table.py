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
    """

    df = sample_pandas_df()

    sharptable.tables
