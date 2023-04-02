from .wrappers_memory import profile
from .wrappers_speed import speedometer

# Implementation of heapsort in Python

# Procedure to convert to a binary heap a subtree with root node i, which is an index in arr[]. n - heap size


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # check if exists left child elem > root

    if l < n and arr[i] < arr[l]:
        largest = l

    # check if exists right child elem > root

    if r < n and arr[largest] < arr[r]:
        largest = r

    # replace root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # свап

        # heapify to root.
        heapify(arr, n, largest)


# main func
@speedometer
def heapSort(arr):
    n = len(arr)

    # building max-heap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # one after one taking out elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # свап
        heapify(arr, i, 0)


@profile
def heapSortMem(arr):
    n = len(arr)

    # building max-heap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # step by step taking out elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # свап
        heapify(arr, i, 0)
