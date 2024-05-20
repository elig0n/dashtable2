About
=====
**dashtable** has functions for converting data to `reStructuredText`
tables and `Markdown` tables, as well as methods for generating data from
these text-tables.

**dashtable2** is the supported **dashtable** fork primary with bugfixes

dashtable2 changelog
----

* 1.4.6
    - add `requirements.txt` required to be installed on the package installation (all deps were optional and required to be installed manually on demand)
    - fix tests
    - substantial code reorganization 

* 1.4.5
    - forked from **dashtable==1.4.5** (https://github.com/doakey3/DashTable) after 6 years without commits
    - update *data2rst* function to raise `NonMergableException` in case of infinite loop

Methods
-------
:html2rst:       Convert html table to `RST grid table`_
:html2md:        Convert html table to Markdown table
:data2md:        Convert a list of lists of strings to Markdown Table
:data2rst:       Convert a list of lists of strings to `RST grid Table`_
:data2md:        Convert a list of lists of strings to a Markdown Table
:data2simplerst: Convert a list of lists of strings to a `simple RST
                 Table`_
:grid2data:      Convert an `RST grid table`_ to data
:simple2data:    Convert a `simple RST table`_ to data

.. _RST grid table: http://docutils.sourceforge.net/docs/user/rst/quickref.html#tables
.. _simple RST Table: http://docutils.sourceforge.net/docs/user/rst/quickref.html#tables
