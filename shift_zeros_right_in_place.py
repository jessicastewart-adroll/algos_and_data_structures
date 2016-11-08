'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
Test Cases:
Input :  [0, 1, 0, 3, 12]
Output : [1, 3, 12, 0, 0]
Input :  [1, 2, 0, 4]
Output : [1, 2, 4, 0]
Input :  [0, 0, 9, 0, 5, 4]
Output : [9, 5, 4, 0, 0, 0]
'''
def shift_zeros_right_in_place(array):
    lowest_swap_position = 0
    i = 0
    
    while i < len(array):
        if array[i] is not 0:
            array[lowest_swap_position], array[i] = array[i], array[lowest_swap_position]
            lowest_swap_position += 1
            i += 1
        else:
            i += 1
        
    return array  

print(shift_zeros_right_in_place([0, 1, 0, 3, 12]))
print(shift_zeros_right_in_place([1, 2, 4, 0]))
print(shift_zeros_right_in_place([0, 0, 9, 0, 5, 4]))
