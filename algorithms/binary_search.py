def binary_search_iterative(array, size, search_value):
	start = 0
	end = size
	while (start <= end):
		middle = (start+end)//2
		#print(start, middle, end, search_value, array[middle])
		if array[middle] == search_value:
			return middle
		elif search_value < array[middle]:
			end = middle - 1
		else:
			start = middle + 1
	return -1


def binary_search_recursive(array, start, end, search_value):
	if start <= end:
		middle = (start+end)//2
		#print(start, middle, end, search_value, array[middle])
		if array[middle] == search_value:
			return middle
		elif search_value < array[middle]:
			return binary_search_recursive(array, start, middle - 1, search_value)
		else:
			return binary_search_recursive(array, middle + 1, end, search_value)
	return -1


arr = [2, 3, 4, 10, 40]
x = 10

#result = binary_search_iterative(arr, len(arr)-1, x)
result = binary_search_recursive(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")