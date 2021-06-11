from typing import Any, List

import numpy as np
import pandas as pd

from .datastore import Datastore


class PandasDatastore(Datastore):
    """
    Pandas DataFrame backing datastore for table.
    """

    def __init__(self, df: pd.DataFrame):
        """
        Args:
            df: Pandas DataFrame.
        """

        self._df = df

    @property
    def columns(self) -> List[Any]:
        """
        Column labels for the table.
        """

        return self._df.columns

    @property
    def rows(self) -> List[Any]:
        """
        Row labels for the table.
        """

        return self._df.index.values

    @property
    def values(self) -> np.ndarray:
        """
        Data structure for table values.
        """

        return self._df.values
