# please excuse my dear aunt sally
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
  final = []
  # iterate over expression
  while current < len(infix):
    i = infix[current]
    # only care about operators 
    if i not in operator_precedence.keys():
      final.append(i)
    elif not stack or '(' in stack:
      # keep acruing until end of parens 
      if i == ')':
        val = stack.pop()
        while val != '(': 
          final.append(val)
          val = stack.pop()
      else:    
        stack.append(i)
    elif i == '(':
      stack.append(i)  
    # save greater preced   
    elif operator_precedence[i] > operator_precedence[stack[-1]]:
      stack.append(i)  
    # pop less preced    
    elif operator_precedence[i] == operator_precedence[stack[-1]]:
      val = stack.pop()
      if val not in [')', '(']:
        final.append(val)
      stack.append(i)
    elif operator_precedence[i] < operator_precedence[stack[-1]]:
      val = stack.pop()
      if val not in [')', '(']:
        final.append(val)
        # compare again
        current-=1
    current+=1
        

  while stack:
    val = stack.pop()
    if val not in [')', '(']:
      final.append(val)
      
        
infix_one = ['A', '*', 'B', '+', 'C']  
infix_two = ['A', '+', 'B', '*', 'C']  
infix_three = ['A', '*', '(', 'B', '+', 'C', ')'] 
infix_four = ['A', '-', 'B', '+', 'C']  
infix_five = ['A', '*', 'B', '^', 'C', '+', 'D']
infix_six = ['A', '*', '(', 'B', '+', 'C', '*', 'D', ')', '+', 'E']
postfix = infix_to_postfix(infix_five)
