import os.path
import sys

sys.path.append('../')

from dashtable.dashutils.files import read_file
from dashtable.dashutils.profile import PROFILE_ENABLED, profile
from dashtable.data2rst import data2rst_enhanced, data2rst_v2


SCRIPT_DIR = os.path.dirname(__file__)


def main():
    r = data2rst_enhanced(
        {
            (0, 1, 0, 2): 'some text',
            (1, 1, 1, 1): 'other\ntext',
            (1, 2, 2, 3): 'other',
        }
    )

    print(r)


def main2():

    table = read_file(os.path.join(SCRIPT_DIR, '../tmp/1500.table.json'))
    spans = read_file(os.path.join(SCRIPT_DIR, '../tmp/1500.spans.json'))

    r = data2rst_v2(table, spans)

    # print(r)


if __name__ == '__main__':
    # main()
    main2()

    if PROFILE_ENABLED:
        n = 'profile_result.txt'
        with open(n, 'w') as f:
            profile.print_stats(output_unit=0.001, stream=f)

        print(f"profiling results are written to {n}")

