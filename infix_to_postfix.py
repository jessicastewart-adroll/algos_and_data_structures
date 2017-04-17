operator_precedence = {
  '^': 1,
  '*': 2,
  '/': 2, 
  '+': 3,
  '-': 3,  
}

def infix_to_postfix(infix):
  stack = []
  for i in infix:
    if type(i) == int:
      print(i)
    elif i == '(':
      stack.append(i)
    elif i == ')':
      found = False
      while not found: 
        val = stack.pop()
        print(val)
        if val == '(':
          found = True
    else:
      if not stack or operator_precedence.get(i, 0) < operator_precedence.get(stack[-1], 0):
        stack.append(i)
      else:
        while operator_precedence.get(i, 0) > operator_precedence.get(stack[-1], 0):
          print(stack.pop())
        
infix_example = [1, '+', 2, '*', '(', 3, '^', 4, '-', 5, ')', '^', '(', 6, '+', 7, '*', 8, ')', '-', 9]   
infix_to_postfix(infix_example)
