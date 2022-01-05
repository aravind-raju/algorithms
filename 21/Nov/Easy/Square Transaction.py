#Problem Name: Square Transaction
#Problem Link:https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/square-transaction-20/

# Time out error
n = int(input())
lst = list(map(int, input().split()))
m = int(input())
targets = []
for _ in range(m):
    i = int(input())
    total = 0
    flag = True
    for j in range(n):
        total += lst[j]
        if total >= i:
            flag = False
            break
    if flag:
        print(-1)
    else:
       print(j+1)



# bisect algorithms using the module “bisect” which allows to keep the list in sorted order after insertion of each element
import bisect

T = int(input())

total, res_arr = 0, []

for each in input().split():

    total=total+int(each)

    res_arr.append(total)

target = int(input())

for _ in range(target):

    num = int(input())

    print(-1) if num>res_arr[len(res_arr)-1] else print(bisect.bisect_left(res_arr,num)+1)
