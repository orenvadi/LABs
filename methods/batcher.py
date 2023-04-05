"""
Python program for Bitonic Sort.
Note that this program works only when size of input is a power of 2.
"""
from __future__ import annotations

from .wrappers_memory import profile
from .wrappers_speed import speedometer


def comp_and_swap(array: list[int], index1: int, index2: int, direction: int) -> None:
    """Compare the value at given index1 and index2 of the array and swap them as per
    the given direction.
    The parameter direction indicates the sorting direction, ASCENDING(1) or
    DESCENDING(0); if (a[i] > a[j]) agrees with the direction, then a[i] and a[j] are
    interchanged.
    """
    if (direction == 1 and array[index1] > array[index2]) or (
        direction == 0 and array[index1] < array[index2]
    ):
        array[index1], array[index2] = array[index2], array[index1]


def bitonic_merge(array: list[int], low: int, length: int, direction: int) -> None:
    """
    It recursively sorts a bitonic sequence in ascending order, if direction = 1, and in
    descending if direction = 0.
    The sequence to be sorted starts at index position low, the parameter length is the
    number of elements to be sorted.
    """
    if length > 1:
        middle = int(length / 2)
        for i in range(low, low + middle):
            print(array)
            comp_and_swap(array, i, i + middle, direction)
        bitonic_merge(array, low, middle, direction)
        bitonic_merge(array, low + middle, middle, direction)


@speedometer
def bitonic_sort(array: list[int], low: int, length: int, direction: int) -> None:
    """
    This function first produces a bitonic sequence by recursively sorting its two
    halves in opposite sorting orders, and then calls bitonic_merge to make them in the
    same order.
    """
    if length > 1:
        middle = int(length / 2)
        bitonic_sort(array, low, middle, 1)
        bitonic_sort(array, low + middle, middle, 0)
        bitonic_merge(array, low, length, direction)


@profile
def bitonic_sortMem(array: list[int], low: int, length: int, direction: int) -> None:
    if length > 1:
        middle = int(length / 2)
        bitonic_sort(array, low, middle, 1)
        bitonic_sort(array, low + middle, middle, 0)
        bitonic_merge(array, low, length, direction)
