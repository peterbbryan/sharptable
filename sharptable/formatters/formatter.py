from abc import ABC, abstractmethod

from sharptable.tables import Table


class Formatter(ABC):
    """
    ABC for sharptable table types.
    """

    @abstractmethod
    def apply(self, table: Table):
        """
        Apply transform to sharptable.
        """

        raise NotImplementedError
