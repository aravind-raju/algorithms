class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def strStr(self, A, B):
		if len(A) == 0 or len(B) == 0:
			return -1
		i = 0
		while i < len(A):
			if A[i] == B[0]:
				j = 0
				ans = i
				while j < len(B) and i < len(A) and A[i] == B[j]:
					i += 1
					j += 1
				if j >= len(B):
					return ans
				if i >= len(A):
					return -1
				i = ans
			i = i + 1
		return -1