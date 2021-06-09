import pandas as pd

import sharptable


def _sample_pandas_df() -> pd.DataFrame:
    """
    Sample DataFrame for basic testing and experimentation.

    Returns:
        TODO
    """

    df = pd.DataFrame([{"a": 1, "b": 2}, {"a": 3, "b": 4}])
    return df


def test_basic_table_visualization() -> None:
    """
    Basic plotting test.
    """

    dataframe = _sample_pandas_df()

    datastore = sharptable.datastores.PandasDatastore(dataframe)
    table = sharptable.tables.MatplotlibTable(datastore)

    table.show()


def test_basic_table_save() -> None:
    """
    """

    dataframe = _sample_pandas_df()

    datastore = sharptable.datastores.PandasDatastore(dataframe)
    table = sharptable.tables.MatplotlibTable(datastore)

    table.savefig("temp")
