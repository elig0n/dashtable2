
import os
import sys
from pathlib import Path

PROJECT_PATH = Path(__file__).parents[1]

sys.path.insert(0, str(PROJECT_PATH))

import dashtable
from dashtable.utils.files import read_text

test_docs = os.path.join(PROJECT_PATH, 'tests', 'static')

for file in os.listdir(test_docs):
    if file.endswith('.html'):
        text = read_text(os.path.join(test_docs, file))

        data, spans, use_headers = dashtable.html2data(text)
        if not data == '':
            table = dashtable.data2rst(data, spans, use_headers=True, center_cells=True, center_headers=True)
            try:
                print(table)
            except UnicodeEncodeError:
                print(table.encode('utf-8'))
