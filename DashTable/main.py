""" Program to convert an html file (example: input.html) with a table inside it
    to an ASCII table.
    Caveats: take into consideration the spans: rowspan and columnspan
"""

from . import dashTable
from . import html2list

def main(file_path):
    # get the table
    datalist, rowspan_list, colspan_list = html2list.html2list(file_path)
    #  result = table_list_to_ascii(table, colspan_list, rowspan_list)
    result = dashTable.table_list_to_ascii(datalist, rowspan_list, colspan_list)
    return result
