from typing import (
    TYPE_CHECKING,
    Never,
    assert_type,
    cast,
)

import arrlib as np
import idxlib as pd

left = cast(pd.Index[bool], ...)

b = np.array([True, False, True], np.bool_)
s = np.array([np.datetime64(f"2025-10-{day:02d}") for day in (1, 2, 3)], np.datetime64)
d = np.array([np.timedelta64(second + 1, "s") for second in range(3)], np.timedelta64)

def test(left: pd.Index[bool], b: np.array([True, False, False]))
assert_type(left * b, pd.Index[bool])

if TYPE_CHECKING:
    assert_type(left * s, Never)
    assert_type(left * d, Never)
