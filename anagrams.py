from collections import defaultdict 

def is_anagram_count(string1, string2):
	count = defaultdict(lambda: 0)
	if len(string1) != len(string2):
		return False

	for i in range(0, len(string1)):
		count[string1[i]] += 1
		count[string2[i]] -= 1

	for k, v in count.items():
		if count[k]:
			return False

	return True			


print(is_anagram_count('hello', 'world')) # False	
print(is_anagram_count('abba', 'baab'))	# True
print(is_anagram_count('a', 'a')) # True	
print(is_anagram_count('a', 'ab')) # False	
print(is_anagram_count('hannah', 'hannah')) # True	
print(is_anagram_count('racecar', 'racecar')) # True	

###
def partition(array, start, end):
	pivot = end

	for i in range(start, end):
		if array[i] > array[pivot] and i < pivot:
			array[i], array[pivot] = array[pivot], array[i]
			pivot = i
		if array[i] < array[pivot] and i > pivot:
			array[i], array[pivot] = array[pivot], array[i]
			pivot = i
	return pivot


def qsort(array, start, end):
	if start >= end:
		return array

	pivot = partition(array, start, end)

	qsort(array, pivot+1, end)
	qsort(array, start, pivot-1)	

	return array		


def is_anagram_sort(string1, string2):
	if len(string1) != len(string2):
		return False

	s1 = qsort(list(string1), 0, len(string1)-1)
	s2 = qsort(list(string2), 0, len(string2)-1)

	return s1 == s2


print(is_anagram_sort('hello', 'world'))	
print(is_anagram_sort('abba', 'baab'))	
