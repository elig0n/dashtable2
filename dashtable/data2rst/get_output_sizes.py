
from .aliases import DATA_TABLE

from ..dashutils.aliases import DATA_SPANS
from ..dashutils.spans import get_longest_line_length, get_span_column_count, get_span_row_count, get_span, \
    get_span_index, convert_spans_to_array


# @profile
def get_output_column_widths(table: DATA_TABLE, spans: DATA_SPANS):
    """
    Gets the widths of the columns of the output table

    Parameters
    ----------
    table : list of lists of str
        The table of rows of text
    spans : list of lists of int
        The [row, column] pairs of combined cells

    Returns
    -------
    widths : list of int
        The widths of each column in the output table
    """
    widths = []
    for column in table[0]:
        widths.append(3)

    spans_arr = convert_spans_to_array(spans)

    for row in range(len(table)):
        for column in range(len(table[row])):
            span = spans[get_span_index(spans_arr, row, column)]
            column_count = get_span_column_count(span)

            if column_count == 1:
                text_row = span[0][0]
                text_column = span[0][1]

                text = table[text_row][text_column]

                length = get_longest_line_length(text)
                if length > widths[column]:
                    widths[column] = length

    for row in range(len(table)):
        for column in range(len(table[row])):
            span = spans[get_span_index(spans_arr, row, column)]
            column_count = get_span_column_count(span)

            if column_count > 1:
                text_row = span[0][0]
                text_column = span[0][1]

                text = table[text_row][text_column]

                end_column = text_column + column_count

                available_space = sum(
                    widths[text_column:end_column])
                available_space += column_count - 1

                length = get_longest_line_length(text)

                while length > available_space:
                    for i in range(text_column, end_column):
                        widths[i] += 1

                        available_space = sum(
                            widths[text_column:end_column])

                        available_space += column_count - 1
                        if length <= available_space:
                            break
    return widths


def get_output_row_heights(table: DATA_TABLE, spans: DATA_SPANS):
    """
    Get the heights of the rows of the output table.

    Parameters
    ----------
    table : list of lists of str
    spans : list of lists of int

    Returns
    -------
    heights : list of int
        The heights of each row in the output table
    """
    heights = []
    for row in table:
        heights.append(-1)

    spans_arr = convert_spans_to_array(spans)

    for row in range(len(table)):
        for column in range(len(table[row])):
            text = table[row][column]
            span = spans[get_span_index(spans_arr, row, column)]
            row_count = get_span_row_count(span)
            height = len(text.split('\n'))
            if row_count == 1 and height > heights[row]:
                heights[row] = height

    for row in range(len(table)):
        for column in range(len(table[row])):
            span = spans[get_span_index(spans_arr, row, column)]
            row_count = get_span_row_count(span)
            if row_count > 1:
                text_row = span[0][0]
                text_column = span[0][1]

                end_row = text_row + row_count

                text = table[text_row][text_column]

                height = len(text.split('\n')) - (row_count - 1)

                add_row = 0
                while height > sum(heights[text_row:end_row]):
                    heights[text_row + add_row] += 1
                    if add_row + 1 < row_count:
                        add_row += 1
                    else:
                        add_row = 0
    return heights
