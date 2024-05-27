
import os
import sys

sys.path.append('../')

from dashtable.dashutils.files import read_json, write_text
from dashtable.exceptions import NonMergableException
from dashtable.data2rst import data2rst


def hide_table_text(table, prefix: str = 'txt '):
    k = 0
    for row in table:
        for i, t in enumerate(row):
            if t:
                lines = t.split('\n')
                for j, v in enumerate(lines):
                    if v:
                        lines[j] = f"{prefix}{k}"
                        k += 1
                row[i] = '\n'.join(lines)
    return table


def main():

    folder = (
        # '../tests/in-out/many-spans'
        'tmp'
        # 'data'
    )

    table = read_json(os.path.join(folder, 'table.json'))
    spans = read_json(os.path.join(folder, 'spans.json'))

    # import json
    # write_text(
    #     os.path.join(folder, 'table-fake.json'),
    #     json.dumps(hide_table_text(table), indent=1)
    # )

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
