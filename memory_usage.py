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

for i in range(100):
    random.shuffle(arr)
    ls.append(arr)


####################################### Batcher Sort #############################################
exec_memory_bitonic = [
    [i, bitonic_sortMem(ls[i], 0, 128, 1)] for i in range(100)
]  # works


data = np.array(exec_memory_bitonic)

x, y = data.T
plt.scatter(x, y)
plt.ylabel("Потребление памяти в байтах")
plt.xlabel("Запуски программы сортировки")
# plt.show()
plt.savefig("plots/batcher_memory.png", dpi=300)  # savefig, don't show
####################################### Batcher Sort #############################################


####################################### Pyramid Sort #############################################
exec_memory_heap = [[i, heapSortMem(ls[i])] for i in range(100)]  # works

data = np.array(exec_memory_heap)

x, y = data.T
plt.scatter(x, y)
plt.ylabel("Потребление памяти в байтах")
plt.xlabel("Запуски программы сортировки")
# plt.show()
plt.savefig("plots/bitonic_memory.png", dpi=300)  # savefig, don't show
####################################### Pyramid Sort #############################################


####################################### Priority Sort #############################################
exec_memory_priority = [
    [i, priority_sortMem(ls[i])] for i in range(100)
]  # for heapSort only

data = np.array(exec_memory_priority)

x, y = data.T
plt.scatter(x, y)
plt.ylabel("Потребление памяти в байтах")
plt.xlabel("Запуски программы сортировки")
# plt.show()
plt.savefig("plots/priority_memory.png", dpi=300)  # savefig, don't show
####################################### Priority Sort #############################################
