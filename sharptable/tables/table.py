from abc import ABC, abstractmethod
from typing import Optional

from sharptable.datastores import Datastore
from sharptable.formatters import Formatter


class Table(ABC):
    """
    ABC for sharptable table types.
    """

    def __init__(self, datastore: Datastore):
        """
        Args:
            datastore: sharptable datastore.
        """

        self._datastore = datastore
        self._formatter: Optional[Formatter] = None

    @property
    def formatter(self) -> Optional[Formatter]:
        """ Formatter getter """

        return self._formatter

    @formatter.setter
    def formatter(self, value: Optional[Formatter]) -> None:
        """ Formatter setter """

        self._formatter = value

    @abstractmethod
    def _apply_formatter(self) -> None:
        """
        Apply all formatters.
        """

        raise NotImplementedError

    @abstractmethod
    def show(self) -> None:
        """
        Show table in interactive sessions.
        """

        raise NotImplementedError

    @abstractmethod
    def savefig(self, path: str, extension: str = ".png") -> None:
        """
        Save table to path.

        Args:
            path: Path to write table to.
        """

        raise NotImplementedError
