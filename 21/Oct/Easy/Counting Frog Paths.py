#Problem Name: Counting Frog Paths
#Problem Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/counting-frog-paths-1abd84d5/
count = 0
X, Y, s, T = map(int, input().split())
for i in range(X, X+s+1):
    for j in range(Y, Y+s+1):
        if i+j <= T:
            count +=1

print(count)