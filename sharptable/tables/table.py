from abc import ABC, abstractmethod

from sharptable import datastores
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

    @abstractmethod
    def show(self) -> None:
        """
        Show table in interactive sessions.
        """

        raise NotImplementedError

    @abstractmethod
    def save_fig(self, path: str) -> None:
        """
        Save table to path.
        
        Args:
            path: Path to write table to.
        """

        raise NotImplementedError
