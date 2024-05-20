import os
import sys

import pytest

from pathlib import Path

PROJECT_PATH = Path(__file__).parents[1]

sys.path.insert(0, str(PROJECT_PATH))

import dashtable
from dashtable.utils.files import read_text


STATIC_PATH = os.path.join(PROJECT_PATH, 'tests', 'static')


files = [
    str(p) for p in sorted(Path(STATIC_PATH).glob('*.html'), key=lambda p: p.stem) if p.is_file()
]
assert files


@pytest.mark.parametrize(
    ('path',),
    [(f,) for f in files]
)
def test_html_to_tables(path: str):

    html_path = path
    rst = dashtable.html2rst(html_path)
    md = dashtable.html2md(html_path)

    rst_path = os.path.splitext(path)[0] + '.rst'
    rst_text = read_text(rst_path).rstrip()

    assert rst == rst_text

    md_path = os.path.splitext(path)[0] + '.md'
    md_text = read_text(md_path).rstrip()

    assert md == md_text


