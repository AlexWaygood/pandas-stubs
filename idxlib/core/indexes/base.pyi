from collections.abc import Sequence
from typing import (
    Generic,
    Never,
    TypeVar,
    overload,
)

from _typeshed import SupportsRMul

from idxlib._typing import (
    np_ndarray_dt,
    np_ndarray_td,
)

T = TypeVar("T")
T_contra = TypeVar("T_contra", contravariant=True)
T_rmul = TypeVar("T_rmul")


class Index(Generic[T]):
    @overload
    def __mul__(self, other: np_ndarray_dt) -> Never: ...
    @overload
    def __mul__(self: "Index[bool] | Index[complex]", other: np_ndarray_td) -> Never: ...
    @overload
    def __mul__(
        self: "Index[T_contra]",
        other: SupportsRMul[T_contra, T_rmul]
        | Sequence[SupportsRMul[T_contra, T_rmul]],
    ) -> "Index[T_rmul]": ...
