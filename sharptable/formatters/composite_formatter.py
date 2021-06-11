from typing import List, Optional

from .formatter import Formatter


class CompositeFormatter(Formatter):
    """
    Class allowing for multiple formatters to be applied.
    """

    def __init__(self, formatters: Optional[List[Formatter]] = None):
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
