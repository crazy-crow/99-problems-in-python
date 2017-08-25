# P1
def my_last(alist):
    return alist[-1]
    
# P2
def my_last_but_one(alist):
    return alist[-2]
    
# P3
def my_kth(alist, k):
    return alist[k]
    
# P4
def my_length(alist):
    i = 0
    for element in alist:
        i = i + 1
    return i
   
# P5
def my_reverse(alist):
    result_list = []
    for element in alist:
        result_list.insert(0, element)
    return result_list