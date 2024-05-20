import os
import sys
import unittest
import ntpath

from pathlib import Path

PROJECT_PATH = Path(__file__).parents[1]

sys.path.insert(0, str(PROJECT_PATH))

import dashtable
from dashtable.utils.files import read_text


class TestMatches(unittest.TestCase):
    def setUp(self):
        self.static_path = os.path.join(PROJECT_PATH, 'tests', 'static')

    def test_html_to_tables(self):
        for file in os.listdir(self.static_path):

            if file.endswith('.html'):
                html_path = os.path.join(self.static_path, file)
                rst = dashtable.html2rst(html_path)
                md = dashtable.html2md(html_path)

                rst_name = os.path.splitext(file)[0] + '.rst'
                rst_path = os.path.join(self.static_path, rst_name)
                rst_text = read_text(rst_path).rstrip()

                try:
                    self.assertEqual(rst, rst_text)
                except AssertionError:
                    print('MATCH ERROR: ' + ntpath.basename(html_path))


                md_name = os.path.splitext(file)[0] + '.md'
                md_path = os.path.join(self.static_path, md_name)
                md_text = read_text(md_path).rstrip()

                try:
                    self.assertEqual(md, md_text)
                except AssertionError:
                    print('MATCH ERROR: ' + ntpath.basename(html_path))


if __name__ == '__main__':
    unittest.main()

