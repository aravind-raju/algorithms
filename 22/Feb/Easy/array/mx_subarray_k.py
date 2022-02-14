"""Question:
Given an array of integers of size ‘n’.
Our aim is to calculate the maximum sum of ‘k’ 
consecutive elements in the array."""

def max_sum_k(array, k, n):
	current_sum = 0
	max_sum = 0
	for i in range(n - k + 1):
		current_sum = sum(x[i:i+k])
		max_sum = max(max_sum, current_sum)
	print(max_sum)

def max_sum_sliding_window(array, k, n):
	if n < k:
		print("Invalid input")
	current_sum = sum(array[:k])
	max_sum = current_sum		
	for i in range(n - k):
		current_sum = current_sum - array[i] + array[i+k]
		max_sum = max(max_sum, current_sum)
	print(max_sum)


x = [1, 4, 2, 10, 23, 3, 1, 0, 20]
#x = [100, 200, 300, 400]
k = 4
size = len(x)
max_sum_k(x, k, size)
max_sum_sliding_window(x, k, size)