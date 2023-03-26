"""
Удалить из массива элемент,
расположенный перед максимальным элементом.
Если удаление элемента невозможно, выдать об этом сообщение.
"""


def remove_before_max(nums: list[int]):
    # finding max value

    val_max = 0
    ind_max = 0
    for ind, num in enumerate(nums):
        if num > val_max:
            val_max = num
            ind_max = ind

    k = -1

    for i in range(0, len(nums)):
        if i != ind_max - 1:  # elem before max
            k += 1
            nums[k] = nums[i]
    del nums[-1]
    return len(nums)


a = [1, 5, 6, 2, 3, 4, 5, 9, 6, 7, 8]
remove_before_max(a)
print(a)
