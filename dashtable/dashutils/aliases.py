from typing import Sequence, Tuple

from typing_extensions import TypeAlias

DATA_SPAN: TypeAlias = Sequence[Tuple[int, int]]
"""(row, column) pairs for each span cells"""

DATA_SPANS: TypeAlias = Sequence[DATA_SPAN]
"""spans sequence"""


