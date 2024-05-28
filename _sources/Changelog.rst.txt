Changelog
=====

* 1.4.14
    * `data2rst`
        - speed up some cell properties

* 1.4.13
    - move `dashtable.utils` logic to `dashtable.dashutils`

* 1.4.12
    - import fixes

* 1.4.11
    * `data2rst`
        - fix case when sometimes successful result recognizes as infinite loop
        - add arguments `candidates_mask_creator` and `checked_mask_creator` with an ability to select and even implement custom versions to speed up `data2rst` merge step
        - create `DATA_TABLE`, `DATA_SPANS` aliases and use them in many places
        - some functions refactor
        - substantial speed up of `get_output_column_widths`, `get_output_row_heights`, `table_cells_2_spans` functions

* 1.4.10
    - spans fixes

* 1.4.9
    - `merge_all_cells` function (`data2rst` part) substantial speed up 
    - fixes on spans format

* 1.4.8
    - same fix as **1.4.7** but for LEFT and RIGHT

* 1.4.7
    - fix `merge_cells` error on complicated TOP and BOTTOM cases

* 1.4.6
    - add `requirements.txt` required to be installed on the package installation (all deps were optional and required to be installed manually on demand)
    - fix tests
    - substantial code and documentation reorganization 
    - automatic tests

* 1.4.5
    - forked from **dashtable==1.4.5** (https://github.com/doakey3/DashTable) after 6 years without commits
    - update *data2rst* function to raise `NonMergableException` in case of infinite loop


