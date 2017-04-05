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
