x = [0, 1, 2, 0, 1, 2]

def dutch_national_flag(x):
	count = {}
	for i in x:
	    if not count.get(i, None):
	            count[i] = 1
	    else:
	    	count[i] += 1
	print([0]*count[0]+[1]*count[1]+[2]*count[2])

def sort012(a, arr_size):
    lo = 0
    hi = arr_size - 1
    mid = 0
    while mid <= hi:
        if a[mid] == 0:
            a[lo], a[mid] = a[mid], a[lo]
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 1:
            mid = mid + 1
        else:
            a[mid], a[hi] = a[hi], a[mid]
            hi = hi - 1
    return a

dutch_national_flag(x)
sort012(x, len(x))