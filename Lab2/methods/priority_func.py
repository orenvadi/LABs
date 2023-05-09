from .wrappers_memory import profile
from .wrappers_speed import speedometer


@speedometer
def priority_sort(nums: list[int]):
    queue = []
    for num in nums:
        q_insert(queue, num)
        print(queue)
    nums = queue


@profile
def priority_sortMem(nums: list[int]):
    queue = []
    for num in nums:
        q_insert(queue, num)
    nums = queue


def q_insert(queue: list, num):
    # if queue is empty
    if len(queue) == 0:
        # add the new num
        queue.append(num)
    else:
        # traverse the queue to find the right place for new num
        for x in range(0, len(queue)):
            # if the of new num is greater
            if num >= queue[x]:
                # if we have traversed the complete queue
                if x == (len(queue) - 1):
                    # add new num at the end
                    queue.insert(x + 1, num)
                else:
                    continue
            else:
                queue.insert(x, num)
                return True
