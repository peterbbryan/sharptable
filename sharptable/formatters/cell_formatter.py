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

    def row(self) -> int:
        """
        Row number of the cell being formatted.
        """

        return self._row

    def column(self) -> int:
        """
        Column number of the cell being formatted
        """

        return self._column
