#Input: arr[] = {3, 2, 1, 4}
#Output: 7
#Explanation: Following are the possible decreasing subarrays with difference 1. 
#[3], [2], [1], [4], [3,2], [2,1], and [3,2,1]
#Therefore, the answer is 7. 

#Input: arr[] = {5, 4, 3, 2, 1, 6}
#Output: 16

def getcount(arr):
    ans = len(arr)
    count = 0
    for i in range(1, len(arr)):
        if (arr[i - 1] - arr[i] == 1):
            count+=1
        else:
            count = 0
        ans = ans + count
    return ans