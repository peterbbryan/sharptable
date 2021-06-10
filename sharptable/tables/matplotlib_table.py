import pathlib
from typing import Tuple

import matplotlib
import matplotlib.pyplot as plt

from sharptable.datastores import Datastore
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

    @staticmethod
    def _get_bounding_box(padding_px: int) -> Tuple:
        """
        TODO fix type hint and returns to use savefig
        """

        del padding_px

        return ()

    def savefig(self, path: str, extension: str = ".png") -> None:
        """
        Save table to path.

        Args:
            path: Path to write table to.
            extension: TODO
        """

        save_path = pathlib.Path(path).with_suffix(extension)

        self._fig.canvas.draw()
        # get bounding box of table
        points = self._table.get_window_extent(plt.gcf()._cachedRenderer).get_points()
        # add 10 pixel spacing
        points[0, :] -= 10
        points[1, :] += 10
        # get new bounding box in inches
        nbbox = matplotlib.transforms.Bbox.from_extents(points / plt.gcf().dpi)

        self._fig.savefig(save_path, bbox_inches=nbbox)

    def show(self) -> None:
        """
        Show table in interactive sessions.
        """

        self._fig.show()
