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


PathLike: TypeAlias = Union[str, os.PathLike]


