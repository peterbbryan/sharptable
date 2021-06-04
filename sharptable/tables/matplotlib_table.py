from sharptable.datastores import Datastore
from sharptable.tables import Table


class MatplotlibTable(Table):
    """
    Matplotlib based table.
    """

    def __init__(self, datastore: Datastore):
        """
        Args:
            datastore: sharptable datastore.
        """

        super().__init__(datastore=datastore)

    def save_fig(self, path: str) -> None:
        """
        Save table to path.
        
        Args:
            path: Path to write table to.
        """

        raise NotImplementedError

    def show(self) -> None:
        """
        Show table in interactive sessions.
        """

        raise NotImplementedError
