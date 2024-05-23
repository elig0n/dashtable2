
import os
import sys

sys.path.append('../')

from dashtable.utils.files import read_json, write_text
from dashtable.exceptions import NonMergableException
from dashtable.data2rst import data2rst


def main():

    folder = (
        # '../tests/in-out/many-spans'
        'tmp'
    )

    table = read_json(os.path.join(folder, 'table.json'))
    spans = read_json(os.path.join(folder, 'spans.json'))

    while True:
        try:
            result = data2rst(table=table, spans=spans, use_headers=False)
        except NonMergableException:
            spans = spans[1:]
        else:
            break

    write_text('./tmp/result.rst.txt', result)


if __name__ == '__main__':
    main()
