from typing import TYPE_CHECKING, Iterable, Optional

from .formatter import Formatter

if TYPE_CHECKING:
    from sharptable.tables import Table


class CompositeFormatter(Formatter):
    """
    Class allowing for multiple formatters to be applied.
    """

    def __init__(self, formatters: Optional[Iterable[Formatter]] = None):
        """
        Args:
            formatters: Optional list of formatters to apply.
        """

        # set list of formatters
        if formatters is None:
            self._formatters = []
        else:
            self._formatters = formatters

    def add(self, formatter: Formatter) -> None:
        """
        Add new formatter to list of formatters.

        Args:
            formatter: Formatter to add to list of formatters.
        """

        self._formatters.append(formatter)

    def apply(self, table: "Table") -> None:
        """
        Apply transform to sharptable.

        Args:
            table: Table that formatter is applied to.
        """

        for formatter in self._formatters:
            formatter.apply(table)
