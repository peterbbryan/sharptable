from abc import ABC, abstractmethod

from sharptable.datastores import Datastore


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
        self._formatter = None

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
