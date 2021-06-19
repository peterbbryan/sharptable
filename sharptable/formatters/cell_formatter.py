from abc import abstractproperty

from sharptable.tables import Table
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

    @abstractproperty
    def row(self) -> int:
        """
        Row number of the cell being formatted.
        """

        return self._row

    @abstractproperty
    def column(self) -> int:
        """
        Column number of the cell being formatted
        """

        return self._column


class BoldCellFormatter(CellFormatter):
    """
    Bold a specific cell.
    """

    def __init__(self, row: int, column: int):
        """
        Args:
            row: *see super*
            column: *see super*
        """

        super().__init__(row=row, column=column)

    def _get_cell(self):
        """
        """

        del self._row
        raise NotImplementedError

    def _matplotlib_apply(self, table: Table) -> None:
        """
        Apply transform to subtype.

        Args:
            table: Table that formatter is applied to.
        """

        del self._row
        del table
        raise NotImplementedError

    def apply(self, table: Table) -> None:
        """
        Apply transform to sharptable.

        Args:
            table: Table that formatter is applied to.
        """

        if isinstance(table, MatplotlibTable):
            self._matplotlib_apply(table)
        else:
            raise NotImplementedError
