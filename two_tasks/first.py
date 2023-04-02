"""
Удалить из массива элемент,
расположенный после максимального элемента.
Если удаление элемента невозможно, выдать об этом сообщение.
"""


def remove_after_max(nums: list[int]):
    # finding max value

    val_max = 0
    ind_max = 0
    for ind, num in enumerate(nums):
        if num > val_max:
            val_max = num
            ind_max = ind

    if ind_max == len(nums) - 1:
        print("max is last element, impossible to remove")
        return -1

    k = -1

    for i in range(0, len(nums)):
        if i != ind_max + 1:  # elem after max
            k += 1
            nums[k] = nums[i]
    del nums[-1]
    return len(nums)


a = [1, 5, 6, 2, 3, 4, 5, 9, 6, 7, 8]
b = [8, 3, 6, 2, 3, 4, 5, 9, 3, 7, 2]
c = [3, 8, 2, 7, 3, 5, 4, 1, 2, 0, 9]
print(f"{a=}")
remove_after_max(a)
print(f"new a={a}")
print(f"{b=}")
remove_after_max(b)
print(f"new b={b}")
print(f"{c=}")
remove_after_max(c)
print(f"new c={c}")
