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
from methods.batcher import bitonic_sort
from methods.priority_func import priority_sort
from methods.pyramid import heapSort

arr = list(range(128))
arr = array("i", arr)  # 'i' - signed int

ls = []

for i in range(100):
    random.shuffle(arr)
    ls.append(arr)


####################################### Batcher Sort #############################################
exec_speeds_bitonic = [[i, bitonic_sort(ls[i], 0, 128, 1)] for i in range(100)]  # works


data = np.array(exec_speeds_bitonic)

x, y = data.T
plt.scatter(x, y)
plt.ylabel("Скорость выполнения в секундах")
plt.xlabel("Запуски программы сортировки")
# plt.show()
plt.savefig("plots/batcher_speed.png", dpi=300)  # savefig, don't show
####################################### Batcher Sort #############################################


####################################### Pyramid Sort #############################################
exec_speeds_heap = [[i, heapSort(ls[i])] for i in range(100)]  # works

data = np.array(exec_speeds_heap)

x, y = data.T
plt.scatter(x, y)
plt.ylabel("Скорость выполнения в секундах")
plt.xlabel("Запуски программы сортировки")
# plt.show()
plt.savefig("plots/bitonic_speed.png", dpi=300)  # savefig, don't show
####################################### Pyramid Sort #############################################


####################################### Priority Sort #############################################
exec_speeds_priority = [
    [i, priority_sort(ls[i])] for i in range(100)
]  # for heapSort only

data = np.array(exec_speeds_priority)

x, y = data.T
plt.scatter(x, y)
plt.ylabel("Скорость выполнения в секундах")
plt.xlabel("Запуски программы сортировки")
# plt.show()
plt.savefig("plots/priority_speed.png", dpi=300)  # savefig, don't show
####################################### Priority Sort #############################################
