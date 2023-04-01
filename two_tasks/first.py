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

    k = -1

    for i in range(0, len(nums)):
        if i != ind_max + 1:  # elem after max
            k += 1
            nums[k] = nums[i]
            print(nums)
    print(nums)
    del nums[-1]
    return len(nums)


a = [1, 5, 6, 2, 3, 4, 5, 9, 6, 7, 8]
remove_after_max(a)
print(a)
