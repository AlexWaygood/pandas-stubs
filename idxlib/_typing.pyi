from typing import Any, TypeAlias

import arrlib as np

np_ndarray_bool: TypeAlias = np.ndarray[tuple[Any, ...], np.dtype[np.bool_]]
np_ndarray_dt: TypeAlias = np.ndarray[tuple[Any, ...], np.dtype[np.datetime64]]
np_ndarray_td: TypeAlias = np.ndarray[tuple[Any, ...], np.dtype[np.timedelta64]]
