from abc import ABC, abstractmethod

from sharptable.tables import Table


class Formatter(ABC):
    """
    ABC for sharptable table types.
    """

    @abstractmethod
    def apply(self, table: Table) -> None:
        """
        Apply transform to sharptable.

        Args:
            table: Table that formatter is applied to.
        """

        raise NotImplementedError
