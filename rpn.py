### binary operators
postfix_example = [5, 1, 2, '+', 4, '×', '+', 3, '−']

def rpn_calculator(postfix):
  values = []
  while postfix:
    current = postfix.pop(0)
    if type(current) == int:
      values.append(current)
    else:
      if not values:
        raise Exception('Invalid input')
      second = values.pop()
      first = values.pop()
      if current == '+':
        current = first + second
      elif current == '−':
        current = first - second  
      elif current == '×':
        current = first * second          
      elif current == '/':
        current = first / second           
      values.append(current)
      
  if len(values) > 1:
    raise Exception('Invalid input')
  else:
    return values.pop(0)
    
print(rpn_calculator(postfix_example))     
