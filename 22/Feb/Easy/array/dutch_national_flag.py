x = [0, 1, 2, 0, 1, 2]

def dutch_national_flag(x):
	count = {}
	for i in x:
	    if not count.get(i, None):
	            count[i] = 1
	    else:
	    	count[i] += 1
	print([0]*count[0]+[1]*count[1]+[2]*count[2])


dutch_national_flag(x)