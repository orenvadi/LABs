# for randomizing
import random
# for fast arrays
from array import array

from prettytable import PrettyTable
# for table
from tabletexifier import Table

# importing sorts
from methods.batcher import bitonic_sort, bitonic_sortMem
from methods.priority_func import priority_sort, priority_sortMem
from methods.pyramid import heapSort, heapSortMem

# for beautifull print
# from pprint import pprint

# for graphs and plots
# import numpy as np
# from matplotlib import pyplot as plt


arr = list(range(128))
arr = array("i", arr)  # 'i' - signed int

ls = []

for i in range(600):
    random.shuffle(arr)
    ls.append(arr)


def save_to_tex(table: Table, path: str):
    with open(path, "w", encoding="utf-8") as file:
        pass
    txt = table.build_latex()
    with open(path, "w", encoding="utf-8") as file:
        file.writelines(txt.split("\n"))

    # Read in the file
    with open(path, "r", encoding="utf-8") as file:
        filedata = file.read()
    # Replace the target string
    filedata = filedata.replace("begin{table}", "begin{table}[H]")
    filedata = filedata.replace(
        "{\\label{Tab:}", ("{" + path.split("/")[2][:-10] + " sort")
    )
    # Write the file out again
    with open(path, "w", encoding="utf-8") as file:
        file.write(filedata)


####################################### Batcher Sort #############################################
exec_speeds_bitonic = [
    [i + 1, bitonic_sort(ls[i], 0, 128, 1), bitonic_sortMem(ls[i + 100], 0, 128, 1)]
    for i in range(40)
]  # works

bitonic_table = Table(
    [
        "Запуск программы",
        "Скорость выполнения",
        "Потребление памяти",
    ],
    table_style="A",
)
# bitonic_table.title = "Batcher sort"

for row in exec_speeds_bitonic:
    bitonic_table.add_row(row)

save_to_tex(bitonic_table, "research_doc/tables/batcher_table.tex")
####################################### Batcher Sort #############################################


####################################### Pyramid Sort #############################################
exec_speeds_heap = [
    [i + 1, heapSort(ls[i + 200]), heapSortMem(ls[i + 300])] for i in range(40)
]  # works

heap_table = Table(
    [
        "Запуск программы",
        "Скорость выполнения",
        "Потребление памяти",
    ],
    table_style="A",
)
# heap_table.title = "Pyramid sort"

for row in exec_speeds_heap:
    heap_table.add_row(row)

save_to_tex(heap_table, "research_doc/tables/pyramid_table.tex")

####################################### Pyramid Sort #############################################


####################################### Priority Sort #############################################
exec_speeds_priority = [
    [i + 1, priority_sort(ls[i + 400]), priority_sortMem(ls[i + 500])]
    for i in range(40)
]  # works

priority_table = Table(
    [
        "Запуск программы",
        "Скорость выполнения",
        "Потребление памяти",
    ],
    table_style="A",
)
# priority_table.title = "Pyramid sort"

for row in exec_speeds_priority:
    priority_table.add_row(row)

save_to_tex(priority_table, "research_doc/tables/priority_table.tex")
####################################### Priority Sort #############################################
