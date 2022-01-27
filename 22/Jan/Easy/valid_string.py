import string

alpha_set = set(string.ascii_lowercase)
def valid_string(value):
	diff = alpha_set.difference(set(value))
	if diff:
		return "Invalid string"
	else:
		return "Valid string"