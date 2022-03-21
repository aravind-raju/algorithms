import bisect 
  
def insert(values, n):
    bisect.insort(values, n)
    return values

def insert_binary(values, n):
    size = len(values)
    index = binary_search_insert(values, size, n)
    values.insert(index, n)
    return values

def binary_search_insert(array, size, search_value):
    start = 0
    end = size
    while (start < end):
        middle = (start+end)//2
        if search_value < array[middle]: 
            end = middle
        else:
            start = middle + 1
    return start

arr1 = [[1, 2, 4], [3, 6], [5, 7]]
lst = arr1[0]  
for i in range(1, len(arr1)):
    for j in arr1[i]:
        #lst = insert(lst, j)
        lst = insert_binary(lst, j)

print(lst)