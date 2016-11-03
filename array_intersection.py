from collections import defaultdict

def get_intersection(array_1, array_2):
    '''Intersection of 2 arrays'''
    counts = defaultdict(int)
    
    array = array_1 + array_2
    
    for value in array:
        counts[value] +=1
        
    return [value for value, count in counts.items() if count == 2]    
        
assert get_intersection([0, 3, 5, 9, 10], [-1, 3, 5, 7, 11]) == [3, 5]  
