import pathlib

import matplotlib.pyplot as plt

from sharptable.datastores import Datastore, PandasDatastore
from sharptable.tables.table import Table


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

        self._table = plt.table(
            cellText=self._datastore.values,
            rowLabels=self._datastore.rows,
            colLabels=self._datastore.columns,
            cellLoc="center",
            rowLoc="center",
            loc="top",
        )

        self._fig = self._table.figure
        self._ax = self._table.axes

        self._ax.set_axis_off()

    def savefig(self, path: str, extension: str = ".png") -> None:
        """
        Save table to path.
        
        Args:
            path: Path to write table to.
            extension: TODO
        """

        save_path = pathlib.Path(path).with_suffix(extension)

        self._fig.savefig(save_path)

    def show(self) -> None:
        """
        Show table in interactive sessions.
        """

        self._fig.show()
