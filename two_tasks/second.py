"""
Вставить заданное значение после каждого элемента массива,
расположенного до первого нулевого элемента.
Если вставка элементов невозможна, выдать об этом сообщение.
"""


def find_zero(arr):
    for i, e in enumerate(arr):
        if e == 0:
            return i


def insert_before_zero(val, arr: list):
    if 0 not in arr or arr[0] == 0:
        print("Error: no zero element found")
        return arr

    c = 0

    for ind, elem in enumerate(arr[: find_zero(arr)]):
        c += 1
        insert_element(arr, ind + c, val)

    return arr


def insert_element(lst, index, element):
    lst.append(None)
    for i in range(len(lst) - 1, index, -1):
        lst[i] = lst[i - 1]
    lst[index] = element
    return lst


val = 10
a = [1, 5, 6, 0, 3, 4, 5, 9, 6, 7, 8]

print(f"{a=}")
a = insert_before_zero(val, a)
print(f"new a={a}")

b = [8, 3, 6, 2, 3, 4, 5, 0, 3, 7, 2]

print(f"{b=}")
b = insert_before_zero(val, b)
print(f"new b={b}")

c = [0, 8, 2, 7, 3, 5, 4, 1, 2, 0, 9]

print(f"{c=}")
c = insert_before_zero(val, c)
print(f"new c={c}")
