"""
useful aliases
"""


from typing import (
    Tuple, Sequence,
    Optional, Union, TypeVar, Literal,
    Hashable
)
from typing_extensions import TypeAlias


import os
import sys

import numpy as np


PathLike: TypeAlias = Union[str, os.PathLike]


array1D: TypeAlias = np.ndarray
array1Dmask: TypeAlias = np.ndarray
array2D: TypeAlias = np.ndarray
array2Dmask: TypeAlias = np.ndarray
