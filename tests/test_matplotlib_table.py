"""
Basic tests to make sure matplotlib tables plot without error.
"""

import pandas as pd

import sharptable


def _sample_pandas_df() -> pd.DataFrame:
    """
    Sample DataFrame for basic testing and experimentation.

    Returns:
        TODO
    """

    dataframe = pd.DataFrame([{"a": 1, "b": 2}, {"a": 3, "b": 4}])
    return dataframe


def test_basic_matplotlib_table_visualization() -> None:
    """
    Basic plotting test. Ensure end to end without failure.
    """

    dataframe = _sample_pandas_df()

    datastore = sharptable.datastores.PandasDatastore(dataframe)
    table = sharptable.tables.MatplotlibTable(datastore)

    table.show()


def test_matplotlib_cell_bolding_single() -> None:
    """
    Test cell bolding.
    """
    # pylint: disable=protected-access

    dataframe = _sample_pandas_df()

    datastore = sharptable.datastores.PandasDatastore(dataframe)
    table = sharptable.tables.MatplotlibTable(datastore)

    bold_formatter = sharptable.formatters.BoldCellFormatter(row=1, column=1)
    table.formatter = bold_formatter

    table.show()

    for cell_id, cell in table.table.get_celld().items():

        if cell_id == (1, 1):
            assert cell._text.get_fontweight() == "bold"
        else:
            assert cell._text.get_fontweight() == "normal"


def test_matplotlib_cell_facecolor_single() -> None:
    """
    Test cell background coloring.
    """
    # pylint: disable=protected-access

    dataframe = _sample_pandas_df()

    datastore = sharptable.datastores.PandasDatastore(dataframe)
    table = sharptable.tables.MatplotlibTable(datastore)

    facecolor_formatter = sharptable.formatters.FacecolorCellFormatter(
        row=1, column=1, color="red"
    )
    table.formatter = facecolor_formatter

    table.show()

    for cell_id, cell in table.table.get_celld().items():

        if cell_id == (1, 1):
            assert cell._facecolor == (1.0, 0.0, 0.0, 1.0)
        else:
            assert cell._facecolor == (1.0, 1.0, 1.0, 1.0)


def test_composite_cell_facecolor_bolding_single_cell():
    """
    Test combination of formatters with the composite formatter, applied to a single cell.
    """
    # pylint: disable=protected-access

    dataframe = _sample_pandas_df()

    datastore = sharptable.datastores.PandasDatastore(dataframe)
    table = sharptable.tables.MatplotlibTable(datastore)

    facecolor_formatter = sharptable.formatters.FacecolorCellFormatter(
        row=1, column=1, color="red"
    )
    bold_formatter = sharptable.formatters.BoldCellFormatter(row=1, column=1)
    composite_formatter = sharptable.formatters.CompositeFormatter(
        formatters=[facecolor_formatter, bold_formatter]
    )
    table.formatter = composite_formatter

    table.show()

    for cell_id, cell in table.table.get_celld().items():

        if cell_id == (1, 1):
            assert cell._facecolor == (1.0, 0.0, 0.0, 1.0)
            assert cell._text.get_fontweight() == "bold"
        else:
            assert cell._facecolor == (1.0, 1.0, 1.0, 1.0)
            assert cell._text.get_fontweight() == "normal"
