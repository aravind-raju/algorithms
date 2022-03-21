def prints(a, n, ind):
    i = ind
    # print from ind-th index to (n+i)th index.
    while i < n + ind :
        print(i % n)
        print(a[(i % n)], end = " ")
        i = i + 1
