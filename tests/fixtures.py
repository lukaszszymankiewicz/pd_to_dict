import numpy as np
import pandas as pd
import pytest


@pytest.fixture
def sample_singleindexed_dataframe():
    return pd.DataFrame(
        data=[[1, 2], [3, 4]],
        columns=["a", "b"],
        index=pd.Index(
            data=["first", "second"],
            name="classification",
        ),
    )


@pytest.fixture
def sample_mulitindexed_dataframe():
    return pd.DataFrame(
        data=np.array([[1, 2, 4, 3], [2, 3, 1, 4], [4, 3, 1, 2], [2, 3, 1, 4]]),
        columns=["James", "John", "Albert", "Michael"],
        index=pd.MultiIndex.from_tuples(
            tuples=[(0, 0), (0, 1), (1, 0), (1, 1)],
            names=["race", "lap"],
        ),
    )
