def pairSum(int_array, total):
    '''
    Find unique pairs of integers that sum to a value.
    input: [50,50,60,40,90,20,10,80,13,12,10,87,97,3,50,80,20], 100
    output: [(50,50),(60,40),(90,10),(80,20),(97,3)]
    '''
    if len(int_array) < 2:
        return 
    seen = set()
    output = set()
    for num in int_array:
        target = total - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))
    print(output)              


pairSum([50,50,60,40,90,20,10,80,13,12,10,87,97,3,50,80,20], 100)
