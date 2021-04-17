# function of Binary Search
import random


def BinarySearch(List, element):
    n = 1
    while(n != 0):
        n = len(List)
        n = n//2
        if element == List[n]:
            return n
        elif element > List[n]:
            List = List[n:]
        else:
            List = List[:n]
    return -1


# test
rndm_List = random.sample(range(1, 11), 10)
rndm_List.sort()
print(rndm_List)
k = BinarySearch(rndm_List, 10)
print(k)
