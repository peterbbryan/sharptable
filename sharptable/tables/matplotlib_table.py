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
