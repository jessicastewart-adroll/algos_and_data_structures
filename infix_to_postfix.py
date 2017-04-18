operator_precedence = {
  ')': 3,
  '(': 3,
  '^': 2,
  '*': 1,
  '/': 1, 
  '+': 0,
  '-': 0,  
}

def infix_to_postfix(infix):
  stack = []
  current = 0
  while current < len(infix):
    i = infix[current]
    if i not in operator_precedence.keys():
      print(i)
    elif not stack or '(' in stack:
      if i == ')':
        val = stack.pop()
        while val != '(': 
          print(val)
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
        print(val)
      stack.append(i)
    elif operator_precedence[i] < operator_precedence[stack[-1]]:
      val = stack.pop()
      if val not in [')', '(']:
        print(val)
        current-=1
    current+=1
        

  while stack:
    val = stack.pop()
    if val not in [')', '(']:
      print(val)
      
        
infix_one = ['A', '*', 'B', '+', 'C']  
infix_two = ['A', '+', 'B', '*', 'C']  
infix_three = ['A', '*', '(', 'B', '+', 'C', ')'] 
infix_four = ['A', '-', 'B', '+', 'C']  
infix_five = ['A', '*', 'B', '^', 'C', '+', 'D']
infix_six = ['A', '*', '(', 'B', '+', 'C', '*', 'D', ')', '+', 'E']
infix_to_postfix(infix_six)
