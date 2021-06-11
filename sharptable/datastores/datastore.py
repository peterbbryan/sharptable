from abc import ABC, abstractproperty
from typing import Any, List


class Datastore(ABC):
    """
    ABC for sharptable datastore types.
    """

    @abstractproperty
    def column_names(self) -> List[Any]:
        """
        Column labels for the table.
        """

        raise NotImplementedError

    @abstractproperty
    def row_names(self) -> List[Any]:
        """
        Row labels for the table.
        """

        raise NotImplementedError

    @abstractproperty
    def values(self) -> Any:
        """
        Data structure for table values.
        """

        raise NotImplementedError
