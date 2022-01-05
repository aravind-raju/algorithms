#Problem Name: Golden rectangles
#Problem Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/almost-golden-rectangular-1c9d72c0/

n = int(input())
count = 0
for i in range(n):
    l, b = map(int, input().split())
    if 1.6<=l/b<=1.7 or 1.6<=b/l<=1.7:
        count += 1

print(count)