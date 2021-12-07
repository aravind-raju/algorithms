from math import sqrt


def jump_search(array, size, search_value):
	n = int(sqrt(size))
	prev_index = -1
	for index in range(0, size, n):
		if search_value < array[index]:
			break
		prev_index = index
	for i in range(prev_index, index):
		if array[i] == search_value:
			return i
	return -1


arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ]
x = 55

result = jump_search(arr, len(arr), x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")