
import os
import sys

import pytest

from pathlib import Path

PROJECT_PATH = Path(__file__).parents[1]

sys.path.insert(0, str(PROJECT_PATH))

import dashtable
from dashtable.utils.files import read_file


STATIC_PATH = os.path.join(PROJECT_PATH, 'tests', 'in-out')


files = [
    str(p) for p in sorted(Path(STATIC_PATH).glob('*'), key=lambda p: p.stem) if p.is_dir()
]
assert files


@pytest.mark.parametrize(
    ('path',),
    [(f,) for f in files]
)
def test_inout(path: str):

    all_files = list(p for p in Path(path).glob('*') if p.is_file())
    for i, p in enumerate(all_files):
        s = p.stem
        try:
            func = getattr(dashtable, s)
        except Exception:
            continue

        kwargs_files = all_files[:i] + all_files[i+1:]

        kwargs = {}
        for kf in kwargs_files:
            kwargs[kf.stem] = read_file(kf)

        defaults = kwargs.pop('defaults', {})
        if defaults:
            kwargs = {**defaults, **kwargs}

        result = read_file(p)

        assert func(**kwargs) == result

        break
    else:
        raise ValueError(f"no file matches a function: {list(map(str, all_files))}")
