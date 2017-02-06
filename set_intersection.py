def set_intersection(first_list, second_list):
  # either list empty case
  if not first_list or not second_list:
    return -1
  
  # no intersection
  if first_list[-1] < second_list[1] or second_list[-1] < first_list[1]:
    return -1
    
  # set-up  
  f = 0
  s = 0
  n = len(first_list)
  output = []
  
  while f < n and s < n:
    if first_list[f] == second_list[s]:
      # check for duplicates
      if len(output) > 0 and output[-1] == first_list[f]:
        f += 1
        s += 1
        continue
      output.append(first_list[f])
      f += 1
      s += 1
    elif first_list[f] > second_list[s]:
      s += 1
    else:
      f += 1
      
  return output    
  
# given 2 ordered lists
first_list = [4, 4, 4, 4, 5, 5]
second_list = [4, 4, 5, 5, 5, 5]
print(set_intersection(first_list, second_list))
