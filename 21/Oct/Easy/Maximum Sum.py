#Problem Name: Maximum Sum
#Problem Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/maximum-sum-4-f8d12458/

n = int(input())
array = list(map(int, input().split()))
total_sum, count = 0, 0

for i in array:
    if i >= 0:
        count += 1
        total_sum += i
if count == 0:
     print(f'{max(array)} 1')
else:
     print(total_sum, count)