# is there a self swap so we get the initial case?
def string_permutations(string, start, end):
	string = list(string)
	if start >= end:
		print(''.join(string))
		return

	for i in range(end-start):
		print('i', i, 'diff', end-start)
		string[i], string[i-1] = string[i-1], string[i]
		string_permutations(string, start, i)
		string[i-1], string[i] = string[i], string[i-1]
		string_permutations(string, start, i)


test = "ABC"
string_permutations(test, 0, len(test))
'''
'ABC'
'ACB'
'BAC'
'BCA'
'CBA'
'CAB'
'''	
