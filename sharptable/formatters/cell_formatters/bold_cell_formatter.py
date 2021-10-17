from typing import TYPE_CHECKING

from sharptable.tables.matplotlib_table import MatplotlibTable

from ..cell_formatter import CellFormatter

if TYPE_CHECKING:
    from sharptable.tables import Table


class BoldCellFormatter(CellFormatter):
    """
    Bold a specific cell.
    """

    def __init__(self, row: int, column: int):
        """
        Args:
            row: Row number of the cell being formatted.
            column: Column number of the cell being formatted
        """

        super().__init__(row=row, column=column)

    def _matplotlib_apply(self, table: MatplotlibTable) -> None:
        """
        Apply transform to subtype.

        Args:
            table: Table that formatter is applied to.
        """

        # get cell being modified
        cell = self._get_matplotlib_cell(table=table)
        cell._text.set_fontweight("bold")  # pylint: disable=protected-access

    def apply(self, table: "Table") -> None:
        """
        Apply transform to sharptable.

        Args:
            table: Table that formatter is applied to.
        """

        if isinstance(table, MatplotlibTable):
            self._matplotlib_apply(table)
        else:
            raise NotImplementedError
