#Write a program to check if all lower case of alphabet is present in the string. 
#You will have an array of string as input and for each individual string you will have to check if which strings satisfy the condition and which doesn't
import string

alphabets = set(string.ascii_lowercase)

def all_alphabets(words):
	for word in words:
		word =  word.lower()
		word_set = set(word)
		s1 = alphabets.difference(word_set)
		s2 = word_set.difference(alphabets)
		flag = s1.union(s2)
		if flag:
			print(word, '- Invalid string')
		else:
			print(word, '- Valid string')


test = ['abcdefghijklmnopqrstuvwxyz', 'abcd$123efghijklmnopqrstuvwxyz', 'uvwxyz']