import pandas as pd

from sharptable.datastores import Datastore


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
