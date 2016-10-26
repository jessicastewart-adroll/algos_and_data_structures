def word_count(sentence):
  '''Print the number of times each word appears in a given sentence. 
    input: "the fox jumps over the fox moon"
    output: 
        the: 2 
        fox: 2
        jumps: 1
        over: 1
        moon: 1
  '''
  output = {}
  word_list = sentence.split()
  for word in word_list: 
    if word in output:
      output[word] += 1
    else:
      output[word] = 1
            
  return output

assert wordCount("the fox jumps over the fox moon") == {"the": 2, "fox": 2, "jumps": 1, "over": 1, "moon": 1}
