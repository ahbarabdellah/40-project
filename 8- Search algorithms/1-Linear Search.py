# algorithm in a function :

def LiniarSearch(List, element):
    '''
    This function return the position of element if it's in the array 
    and -1 if not,
    '''
    n = len(List)
    for i in range(n):
        if element == List[i]:
            return i
    return -1
