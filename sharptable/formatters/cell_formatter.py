import matplotlib

from sharptable.tables.matplotlib_table import MatplotlibTable

from .formatter import Formatter


class CellFormatter(Formatter):
    """
    ABC for sharptable cells.
    """

    def __init__(self, row: int, column: int):
        """
        Args:
            row: Row number of the cell being formatted.
            column: Column number of the cell being formatted
        """

        self._row = row
        self._column = column

    def _get_matplotlib_cell(self, table: MatplotlibTable) -> matplotlib.table.Cell:
        """
        Get matplotlib cell at index.

        Args:
            table: MatplotlibTable containing cell.
        Returns:
            Matplotlib cell from table at the row, col index.
        """

        cell = table.table[self.row, self.column]

        return cell

    @property
    def row(self) -> int:
        """
        Row number of the cell being formatted.
        """

        return self._row

    @property
    def column(self) -> int:
        """
        Column number of the cell being formatted
        """

        return self._column
