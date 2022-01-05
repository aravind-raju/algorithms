#Problem Name: Hexadecimal numbers
#Problem Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/yet-another-easy-problem-1f3273a0/
import math

def hexsum(a):
    total = 0
    for i in hex(a)[2:]:
        total += int(i, 16)
    return total

t = int(input())

for _ in range(t):
    L, R= [int(x) for x in input().split()]
    count = 0
    for j in range(L, R+1):
        if (math.gcd(j, hexsum(j))) > 1:
            count += 1
    print(count)