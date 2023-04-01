"""
Вставить заданное значение после каждого элемента массива,
расположенного до первого нулевого элемента.
Если вставка элементов невозможна, выдать об этом сообщение.
"""


def find_index(arr, element):
    for i, e in enumerate(arr):
        if e == element:
            return i


def insert_before_zero(val, arr: list):
    if 0 not in arr:
        print("Error: no zero element found")
        return arr

    zero_found = 0
    c = 0

    for ind, elem in enumerate(arr[: find_index(arr, 0)]):
        if zero_found < 1:
            c += 1
            insert_element(arr, ind + c, val)
        if elem == 0:
            zero_found += 1

    return arr


def insert_element(lst, index, element):
    lst.append(None)
    for i in range(len(lst) - 1, index, -1):
        lst[i] = lst[i - 1]
    lst[index] = element
    return lst


arr = [1, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9]
val = 10


result = insert_before_zero(val, arr)
print(result)  # Output: [1, 10, 2, 10, 3, 10, 0, 4, 5, 6, 0, 7, 8, 9]
