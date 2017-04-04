def next_lexographical_permutation(string):
	i = len(string)-1
	pivot = -1

	while i > 0:
		if string[i] > string[i-1]:
			pivot = i-1
			break
		i -= 1

	if pivot < 0:
		print(string)
		return

	j = pivot+1
	successor = None
	while j < len(string):
		if string[j] > string[pivot]:
			if not successor:
				successor = j
			else:
				if string[successor] >= string[j]:
					successor = j
		j += 1
	
	string[pivot], string[successor] = string[successor], string[pivot]

	start = pivot+1
	end = len(string)-1

	while start < end:
		string[start], string[end] = string[end], string[start]
		start += 1
		end -= 1

	print(string)	


test = [0, 1, 2, 5, 3, 3, 0]
next_lexographical_permutation(test)
# [0, 1, 3, 0, 2, 3, 5]

test = [5, 4, 3, 2, 1]
next_lexographical_permutation(test)
# [0, 1, 3, 0, 2, 3, 5]
