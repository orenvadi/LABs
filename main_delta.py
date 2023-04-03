# for randomizing
import random
# for fast arrays
from array import array

# for graphs and research_doc/plots
import numpy as np
from matplotlib import pyplot as plt

# importing sorts
from methods.batcher import bitonic_sort
from methods.priority_func import priority_sort
from methods.pyramid import heapSort

arr = list(range(4))
arr = array("i", arr)  # 'i' - signed int

ls = []

for i in range(10):
    random.shuffle(arr)
    ls.append(arr)
    ln_arr = len(arr)
    arr.extend(list(range(ln_arr, ln_arr * 2)))


colors = ["batcher:blue", "priority:orange", "pyramid:green"]
####################################### Batcher Sort #############################################
exec_speeds_bitonic = [
    [2 ** (i + 2), bitonic_sort(ls[i], 0, len(ls[i]), 1)] for i in range(10)
]  # works


data = np.array(exec_speeds_bitonic)

x, y = data.T

plt.scatter(
    x,
    y,
    c=colors[0].split(":")[1],
    label=colors[0],
    alpha=0.3,
    edgecolors="none",
)
plt.ylabel("Скорость выполнения в секундах")
plt.xlabel("Длина сортируемого массива")
plt.legend()
# plt.show()
plt.savefig(
    "research_doc/plots/batcher_speed_delta.png", dpi=400
)  # savefig, don't show
####################################### Batcher Sort #############################################

arr = list(range(4))
arr = array("i", arr)  # 'i' - signed int

ls = []

for i in range(10):
    random.shuffle(arr)
    ls.append(arr)
    ln_arr = len(arr)
    arr.extend(list(range(ln_arr, ln_arr * 2)))

####################################### Priority Sort #############################################
exec_speeds_priority = [
    [2 ** (i + 2), priority_sort(ls[i])] for i in range(10)
]  # for heapSort only

data = np.array(exec_speeds_priority)

x, y = data.T
plt.scatter(
    x,
    y,
    c=colors[1].split(":")[1],
    label=colors[1],
    alpha=0.3,
    edgecolors="none",
)
plt.ylabel("Скорость выполнения в секундах")
plt.xlabel("Длина сортируемого массива")
plt.legend()
# plt.show()
plt.savefig(
    "research_doc/plots/priority_speed_delta.png", dpi=400
)  # savefig, don't show
####################################### Priority Sort #############################################

arr = list(range(4))
arr = array("i", arr)  # 'i' - signed int

ls = []

for i in range(10):
    random.shuffle(arr)
    ls.append(arr)
    ln_arr = len(arr)
    arr.extend(list(range(ln_arr, ln_arr * 2)))

####################################### Pyramid Sort #############################################
exec_speeds_heap = [[2 ** (i + 2), heapSort(ls[i])] for i in range(10)]  # works

data = np.array(exec_speeds_heap)

x, y = data.T
plt.scatter(
    x,
    y,
    c=colors[2].split(":")[1],
    label=colors[2],
    alpha=0.3,
    edgecolors="none",
)
plt.ylabel("Скорость выполнения в секундах")
plt.xlabel("Длина сортируемого массива")
plt.legend()
# plt.show()
plt.savefig(
    "research_doc/plots/bitonic_speed_delta.png", dpi=400
)  # savefig, don't show
####################################### Pyramid Sort #############################################
