"""A module with platform-specific extended precision
`arrlib.number` subclasses.

The subclasses are defined here (instead of ``__init__.pyi``) such
that they can be imported conditionally via the arrlib's mypy plugin.
"""

import arrlib as np

from . import _96Bit, _128Bit

float96 = np.floating[_96Bit]
float128 = np.floating[_128Bit]
complex192 = np.complexfloating[_96Bit, _96Bit]
complex256 = np.complexfloating[_128Bit, _128Bit]
