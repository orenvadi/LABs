# for randomizing
import random

# for fast arrays
from array import array

# for beautifull print
from pprint import pprint

# for graphs and plots
import numpy as np
from matplotlib import pyplot as plt

# importing sorts
from methods.batcher import bitonic_sortMem
from methods.priority_func import priority_sortMem
from methods.pyramid import heapSortMem

arr = list(range(128))
arr = array("i", arr)  # 'i' - signed int

ls = []

for i in range(300):
    random.shuffle(arr)
    ls.append(arr)


colors = ["batcher:blue", "priority:orange", "pyramid:green"]
####################################### Batcher Sort #############################################
exec_memory_bitonic = [
    [i, bitonic_sortMem(ls[i], 0, 128, 1)] for i in range(100)
]  # works


data = np.array(exec_memory_bitonic)

x, y = data.T
plt.scatter(
    x,
    y,
    c=colors[0].split(":")[1],
    label=colors[0],
    alpha=0.3,
    edgecolors="none",
)
plt.ylabel("Потребление памяти в байтах")
plt.xlabel("Запуски программы сортировки")
plt.legend()
# plt.show()
plt.savefig("research_doc/plots/batcher_memory.png", dpi=300)  # savefig, don't show
####################################### Batcher Sort #############################################

####################################### Priority Sort #############################################
exec_memory_priority = [
    [i, priority_sortMem(ls[i + 100])] for i in range(100)
]  # for heapSort only

data = np.array(exec_memory_priority)

x, y = data.T
plt.scatter(
    x,
    y,
    c=colors[1].split(":")[1],
    label=colors[1],
    alpha=0.3,
    edgecolors="none",
)
plt.ylabel("Потребление памяти в байтах")
plt.xlabel("Запуски программы сортировки")
plt.legend()
# plt.show()
plt.savefig("research_doc/plots/priority_memory.png", dpi=300)  # savefig, don't show
####################################### Priority Sort #############################################

####################################### Pyramid Sort #############################################
exec_memory_heap = [[i, heapSortMem(ls[i + 200])] for i in range(100)]  # works

data = np.array(exec_memory_heap)

x, y = data.T
plt.scatter(
    x,
    y,
    c=colors[2].split(":")[1],
    label=colors[2],
    alpha=0.3,
    edgecolors="none",
)
plt.ylabel("Потребление памяти в байтах")
plt.xlabel("Запуски программы сортировки")
plt.legend()
# plt.show()
plt.savefig("research_doc/plots/bitonic_memory.png", dpi=300)  # savefig, don't show
####################################### Pyramid Sort #############################################
