import time

# Write a Python function called is_palindrome that checks if a given word is a palindrome. The function should have proper error handling and be tested with unittest
def is_palindrome(word: str):
  '''

  is_palindrome is a function used to find out if a word says the same backwards.

  This function transforms a string in a list with each letter in each position and uses <list>.reverse() to reverse the letters,  then returns an affirmation if the word is palindrome or not.

  Parameters:
  _______________________
    word: string
      May be a word with no spaces and special characters, because this function is not for palindrome sentences

  Example:
  __________________
    is_palindrome('ana') -> 'The word "ana" is palindrome'
  '''
  rev = list(word.lower())
  rev.reverse()
  pal = ''
  for i in rev:
    pal += i
  if pal == word:
    return f'The word "{word}" is palindrome'
  else:
    return f'The word "{word}" is not palindrome'


# Create a Python decorator called timer that measures the time taken to execute a function. Use this decorator on a function that sorts a list of random numbers and prints the sorted list.


def func_timer(function):
  def temp(*args):
    start = time.time()
    res = function(*args)
    final = time.time() - start
    print(f"El tiempo de ejecucución fue: {final}")
    return res
    
  return temp

@func_timer
def order(lst: list):
  '''
    Orders a list in ascending order

    Takes a list as a parameter and returns a new list with the same values but organized in ascending order

    parameters
    ________________

    list: 
      A list of numeric values

  '''
  res = []
  while len(lst) > 1:
    temp = lst[0]
    for i in lst:
      if temp >= i:
        temp = i
    res.append(temp)
    if temp in lst:
      lst.remove(temp)
  else:
    res.append(lst[0])

  return res