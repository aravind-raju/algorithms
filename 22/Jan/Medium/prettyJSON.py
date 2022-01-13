class Solution:
	# @param A : string
	# @return a list of strings
	def prettyJSON(self, json):
		result = []
		multiplier = 0
		i = 0

		while i < len(json):
			if json[i] in ['{', '[']:
				result.append('\t' * multiplier + json[i])
				multiplier += 1
				i += 1
			elif json[i] in ['}', ']']:
				multiplier -= 1
				result.append('\t' * multiplier + json[i])
				i += 1
			elif json[i] == ',':
				result[-1] += ','
				i += 1
			else:
				start = i
				while i < len(json) and json[i] not in ['{', '}', ',', '[', ']']:
					i += 1
				curr_s = json[start:i]
				result.append('\t' * multiplier + curr_s)

		return result
