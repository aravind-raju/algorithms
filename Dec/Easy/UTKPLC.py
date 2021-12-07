#Problem Name: UTKPLC
#Problem Link: https://www.codechef.com/DEC21C/problems/UTKPLC
n = int(input())
for _ in range(n):
    choice = input().split()
    x, y = input().split()
    if choice.index(x) < choice.index(y):
        print(x)
    else:
        print(y)