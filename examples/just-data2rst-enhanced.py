

import sys

sys.path.append('../')

from dashtable.data2rst import data2rst_enhanced


def main():
    r = data2rst_enhanced(
        {
            (0, 1, 0, 2): 'some text',
            (1, 1, 1, 1): 'other\ntext',
            (1, 2, 2, 3): 'other',
        }
    )

    print(r)


if __name__ == '__main__':
    main()
