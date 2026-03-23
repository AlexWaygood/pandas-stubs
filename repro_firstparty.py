from typing import (
    TYPE_CHECKING,
    Never,
    assert_type,
    cast,
)

import arrlib as np
import idxlib as pd

b = np.array([True, False, True], np.bool_)

def test(left: pd.Index[bool]):
    reveal_type(left * b, pd.Index[bool])

