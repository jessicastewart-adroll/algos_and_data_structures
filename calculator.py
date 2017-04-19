operator_precedence = {
  ')': 3,
  '(': 3,
  '^': 2,
  '*': 1,
  '/': 1, 
  '+': 0,
  '-': 0,  
}

def rpn_converter(infix):
  stack = []
  current = 0
  final = []
  while current < len(infix):
    i = infix[current]
    if i not in operator_precedence.keys():
      final.append(i)
    elif not stack or '(' in stack:
      if i == ')':
        val = stack.pop()
        while val != '(': 
          final.append(val)
          val = stack.pop()
      else:    
        stack.append(i)
    elif i == '(':
      stack.append(i)  
    elif operator_precedence[i] > operator_precedence[stack[-1]]:
      stack.append(i)  
    elif operator_precedence[i] == operator_precedence[stack[-1]]:
      val = stack.pop()
      if val not in [')', '(']:
        final.append(val)
      stack.append(i)
    elif operator_precedence[i] < operator_precedence[stack[-1]]:
      val = stack.pop()
      if val not in [')', '(']:
        final.append(val)
        current-=1
    current+=1

  while stack:
    val = stack.pop()
    if val not in [')', '(']:
      final.append(val)

  return final    


def rpn_calculator(postfix):
  values = []
  result = 0
  while postfix:
    current = postfix.pop(0)
    if current not in operator_precedence.keys():
      values.append(current)
    else:
      if not values:
        raise Exception('Invalid input')
      second = values.pop()
      first = values.pop()
      if current == '+':
        result = first + second
      elif current == '-':
        result = first - second  
      elif current == '*':
        result = first * second          
      elif current == '/':
        result = first // second 
      elif current == '^':
        result = pow(first, second)              
      values.append(result)
      
  if len(values) > 1:
    raise Exception('Invalid input')
  else:
    return values.pop(0)
      
def calculator(infix):
  rpn = rpn_converter(infix)
  return rpn_calculator(rpn)      
        
infix = [5, '*', '(', 7, '-', 10, '/', 2, ')', '+', 4]
print(calculator(infix) == 14)
