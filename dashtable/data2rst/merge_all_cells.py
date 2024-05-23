
from typing import List, Dict, Tuple

from collections import defaultdict

import numpy as np

from ..exceptions import NonMergableException

from .cell import Cell
from .cell import get_merge_direction
from .cell import merge_cells


def merge_all_cells(cells: List[Cell]) -> str:
    """
    Loop through list of cells and piece them together one by one

    Parameters
    ----------
    cells : list of dashtable.data2rst.Cell

    Returns
    -------
    grid_table : str
        The final grid table
    """

    checked = np.zeros((len(cells), len(cells)), dtype=bool)

    current = 0

    while len(cells) > 1:
        count = 0

        while count < len(cells):
            c1 = cells[current]
            c2 = cells[count]

            merge_direction = get_merge_direction(c1, c2)
            if merge_direction is None:

                if checked[current, count]:  # already checked
                    if checked.all():  # if all combinations checked -- raise infinite loop error
                        raise NonMergableException('current cells cannot be merged due to too complicated structure')

                checked[current, count] = True
                count += 1
            else:
                merge_cells(c1, c2, merge_direction)

                if current > count:
                    current -= 1

                cells.pop(count)

                checked = np.zeros((len(cells), len(cells)), dtype=bool)

        current += 1

        if current >= len(cells):
            current = 0

    return cells[0].text

# @profile
# def merge_all_cells(cells: List[Cell]) -> str:
#     """
#     Loop through list of cells and piece them together one by one
#
#     Parameters
#     ----------
#     cells : list of dashtable.data2rst.Cell
#
#     Returns
#     -------
#     grid_table : str
#         The final grid table
#     """
#
#     if len(cells) == 1:
#         return cells[0].text
#
#     #region INITIALS
#
#     prev_cells = {i: c for i, c in enumerate(cells)}
#     """{ cell 'index' -> cell }"""
#     prev_count = len(prev_cells)
#
#     index_to_ltrb: Dict[int, Tuple[int, int, int, int]] = {}
#     """{ cell index -> (left, top, right, bottom }"""
#
#     left_right_to_indexes: Dict[Tuple[int, int], List[int]] = defaultdict(list)
#     """
#     { (left, right) -> [ cells indexes ] }
#
#     used for fast caching
#     """
#
#     top_bottom_to_indexes: Dict[Tuple[int, int], List[int]] = defaultdict(list)
#     """{ (top, bottom) -> [cells indexes] }"""
#
#     #
#     # fill caches
#     #
#     for i, c in prev_cells.items():
#         l, t, r, b = c.left_top_right_bottom
#         index_to_ltrb[i] = (l, t, r, b)
#         left_right_to_indexes[(l, r)].append(i)
#         top_bottom_to_indexes[(t, b)].append(i)
#
#     #endregion
#
#     new_cells: Dict[int, Cell] = {}
#
#     while True:
#
#         if len(prev_cells) < 2:  # there are not enough cells in this storage -- migrate from another storage
#             if len(prev_cells) == 1:
#                 new_cells.update(prev_cells)
#
#             new_count = len(new_cells)
#             if new_count == 1:
#                 break
#             if new_count == prev_count:  # infinite loop started
#                 raise NonMergableException(
#                     'current cells cannot be merged due to too complicated structure'
#                 )
#             prev_cells = new_cells
#             prev_count = new_count
#             new_cells = {}
#
#         i1, c1 = prev_cells.popitem()
#
#         l, t, r, b = index_to_ltrb[i1]
#
#         while True:  # use this cell until it works
#             possible_neighbours = [
#                 i for i in left_right_to_indexes[(l, r)] + top_bottom_to_indexes[(t, b)]
#                 if i != i1
#             ]
#             if not possible_neighbours:
#                 new_cells[i1] = c1
#                 break
#
#             for i2 in possible_neighbours:  # try first mergable
#
#                 if i2 == i1:
#                     continue
#
#                 c2 = prev_cells.get(i2)
#                 if c2 is None:  # this pair is already checked
#                     continue
#
#                 merge_direction = get_merge_direction(c1, c2)
#                 if not merge_direction:  # check if swap works
#                     merge_direction = get_merge_direction(c2, c1)
#                     if merge_direction:  # perform swap to simplify next code
#                         c1, c2 = c2, c1
#
#                 if merge_direction:  # merge and update caches
#                     merge_cells(c1, c2, merge_direction)
#
#                     #
#                     # update caches
#                     #
#                     prev_cells.pop(i2)
#
#                     for i in (i1, i2):
#                         left, top, right, bottom = index_to_ltrb.pop(i)
#                         left_right_to_indexes[(left, right)].remove(i)
#                         top_bottom_to_indexes[(top, bottom)].remove(i)
#
#                     l, t, r, b = c1.left_top_right_bottom
#                     index_to_ltrb[i1] = l, t, r, b
#                     left_right_to_indexes[(l, r)].append(i1)
#                     top_bottom_to_indexes[(t, b)].append(i1)
#
#                     new_cells[i1] = c1
#
#                     break
#
#             else:  # cannot merge with any of neighbours -- just move to next
#                 new_cells[i1] = c1
#                 break
#
#
#     return new_cells.popitem()[1].text

