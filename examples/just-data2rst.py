import sys

sys.path.append('../')

from dashtable.data2rst import data2rst


def main():
    spans = [
        [[3, 1], [4, 1]],
        [[3, 2], [4, 2]],
        [[2, 1], [2, 2]],
    ]
    table = [
        ["Header 1", "Header 2", "Header 3"],
        ["body row 1", "column 2", "column 3"],
        ["body row 2", "Cells may span columns.", ""],
        ["body row 3", "Cells may\nspan rows.", "- Cells\n- contain\n- blocks."],
        ["body row 4", "", ""],
    ]

    r = data2rst(table=table, spans=spans)

    print(r)


if __name__ == '__main__':
    main()


