# for randomizing
import random
# for fast arrays
from array import array

# importing sorts
from methods.batcher import bitonic_sort
from methods.priority_func import priority_sort
from methods.pyramid import heapSort

arr = list(range(8))
random.shuffle(arr)
arr = array("i", arr)  # 'i' - signed int

ls = [arr.__copy__() for _ in range(3)]
print(ls)

####################################### Batcher Sort #############################################
print("**********bitonic***********")
bitonic_sort(ls[0], 0, 8, 1)
print("**********bitonic***********")
####################################### Batcher Sort #############################################

####################################### Priority Sort #############################################
print("**********priority***********")
priority_sort(ls[1])
print("**********priority***********")
####################################### Priority Sort #############################################

####################################### Pyramid Sort #############################################
print("**********pyramid***********")
heapSort(ls[2])
print("**********pyramid***********")
####################################### Pyramid Sort #############################################
print(ls)
