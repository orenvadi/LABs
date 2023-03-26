from pprint import pprint

# for graphs and plots
import numpy as np
from matplotlib import pyplot as plt

# importing sorts
from methods.batcher import bitonic_sort
from methods.priority_func import priority_sort
from methods.pyramid import heapSort

ls = [
    42,
    65,
    68,
    78,
    76,
    85,
    25,
    91,
    90,
    24,
    95,
    26,
    101,
    89,
    117,
    116,
    27,
    74,
    51,
    58,
    105,
    3,
    23,
    21,
    108,
    32,
    113,
    46,
    97,
    106,
    81,
    71,
    11,
    14,
    12,
    104,
    100,
    47,
    111,
    59,
    31,
    40,
    99,
    18,
    79,
    120,
    118,
    62,
    35,
    93,
    123,
    114,
    55,
    22,
    13,
    70,
    37,
    103,
    4,
    44,
    33,
    124,
    7,
    92,
    127,
    86,
    107,
    67,
    119,
    54,
    2,
    19,
    63,
    98,
    126,
    88,
    96,
    17,
    49,
    128,
    84,
    41,
    45,
    125,
    5,
    16,
    39,
    50,
    87,
    72,
    28,
    122,
    73,
    52,
    83,
    109,
    20,
    36,
    110,
    38,
    48,
    112,
    77,
    56,
    6,
    94,
    66,
    34,
    53,
    1,
    121,
    57,
    102,
    69,
    60,
    43,
    64,
    115,
    75,
    82,
    80,
    15,
    61,
    29,
    8,
    10,
    9,
    30,
]


# exec_speeds = [[i, bitonic_sort(ls, 0, 128, 1)] for i in range(100)] # works
# exec_speeds = [[i, heapSort(ls)] for i in range(100)] # works
exec_speeds = [[i, priority_sort(ls)] for i in range(100)]  # for heapSort only


data = np.array(exec_speeds)

# pprint(exec_speeds)

x, y = data.T
plt.scatter(x, y)
plt.ylabel("Скорость выполнения в секундах")
plt.xlabel("Запуски программы сортировки")
# plt.show()
plt.savefig("matplotlib.png")  # savefig, don't show


