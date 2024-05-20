
from dashtable.utils.files import read_json, write_text
from dashtable.data2rst import data2rst


def main():
    table = read_json('../tests/in-out/many-spans/table.json')
    spans = read_json('../tests/in-out/many-spans/spans.json')

    result = data2rst(table=table, spans=spans, use_headers=False)

    write_text('./tmp/result.rst.txt', result)


if __name__ == '__main__':
    main()
