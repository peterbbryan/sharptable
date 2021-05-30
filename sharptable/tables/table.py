from abc import ABC, abstractmethod


class Table(ABC):
    """
    ABC for sharptable table types.
    """

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
