def commonPoint(node, startIndex, endIndex):
	startArray = []
	endArray = []
	start = startIndex
	end = endIndex


	array = [start, end]

	for i in node:

		if node[start] in array:
			return start
		
		if node[end] in array:
			return end

		array.append(node[start])
		array.append(node[end])

		start = node[start]
		end = node[end]

		if start == startIndex or end == endIndex or start == -1 or end == -1:
			return -1

	return -1

 
n = int(input())
for i in range(n):
    m = int(input())
    edges = list(map(int, input().split()))
    startIndex, endIndex = list(map(int, input().split()))
    print(commonPoint(edges, startIndex, endIndex))
    