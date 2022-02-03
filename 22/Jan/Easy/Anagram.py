#Anagram
def check_anagram(array, group):
	output = []
	for i in group:
		p1, p2 = i
		if array[p1-1] == array[p2-1][::-1]:
			output.append(i)
	return output


array = ['cat', 'dog', 'god', 'tc']
print(check_anagram(array, [[1, 4], [2, 3]]))