import os
import sys

import pytest

from pathlib import Path

PROJECT_PATH = Path(__file__).parents[1]

sys.path.insert(0, str(PROJECT_PATH))

import dashtable
from dashtable.dashutils.files import read_text


STATIC_PATH = os.path.join(PROJECT_PATH, 'tests', 'static')


files = [
    str(p) for p in sorted(Path(STATIC_PATH).glob('*.html'), key=lambda p: p.stem) if p.is_file()
]
assert files


@pytest.mark.parametrize(
    ('path',),
    [(f,) for f in files]
)
def test_html_to_tables(
    path: str  # = './static/colspan-rowspan4.html'
):

    html_path = path
    for fmt, converter in (
        ('rst', dashtable.html2rst),
        ('md', dashtable.html2md),
    ):
        fmt_path = os.path.splitext(path)[0] + f'.{fmt}'
        if os.path.exists(fmt_path):
            converted_text = converter(html_path)
            target_text = read_text(fmt_path).rstrip()

            assert converted_text == target_text



