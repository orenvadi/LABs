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

arr = list(range(128))
arr = array("i", arr)  # 'i' - signed int

ls = []

for i in range(300):
    random.shuffle(arr)
    ls.append(arr)


colors = ["batcher:blue", "priority:orange", "pyramid:green"]
####################################### Batcher Sort #############################################
exec_speeds_bitonic = [[i, bitonic_sort(ls[i], 0, 128, 1)] for i in range(100)]  # works


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
plt.xlabel("Запуски программы сортировки")
plt.legend()
# plt.show()
plt.savefig("research_doc/plots/batcher_speed.png", dpi=400)  # savefig, don't show
####################################### Batcher Sort #############################################

####################################### Priority Sort #############################################
exec_speeds_priority = [
    [i, priority_sort(ls[i + 100])] for i in range(100)
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
plt.xlabel("Запуски программы сортировки")
plt.legend()
# plt.show()
plt.savefig("research_doc/plots/priority_speed.png", dpi=400)  # savefig, don't show
####################################### Priority Sort #############################################

####################################### Pyramid Sort #############################################
exec_speeds_heap = [[i, heapSort(ls[i + 200])] for i in range(100)]  # works

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
plt.xlabel("Запуски программы сортировки")
plt.legend()
# plt.show()
plt.savefig("research_doc/plots/bitonic_speed.png", dpi=400)  # savefig, don't show
####################################### Pyramid Sort #############################################
