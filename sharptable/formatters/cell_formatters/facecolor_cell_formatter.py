from typing import TYPE_CHECKING, Tuple, Union

from sharptable.tables.matplotlib_table import MatplotlibTable

from ..cell_formatter import CellFormatter

if TYPE_CHECKING:
    from sharptable.tables import Table


class FacecolorCellFormatter(CellFormatter):
    """
    Color the background of a specific cell.
    """

    def __init__(
        self, row: int, column: int, color: Union[str, Tuple[float, float, float]]
    ):
        """
        Args:
            row: Row number of the cell being formatted.
            column: Column number of the cell being formatted
        """

        super().__init__(row=row, column=column)

        self._color = color

    def _matplotlib_apply(self, table: MatplotlibTable) -> None:
        """
        Apply transform to subtype.

        Args:
            table: Table that formatter is applied to.
        """

        # get cell being modified
        cell = self._get_matplotlib_cell(table=table)
        cell.set_facecolor(self._color)

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
