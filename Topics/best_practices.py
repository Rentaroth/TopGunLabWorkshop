import time

# Write a Python function called is_palindrome that checks if a given word is a palindrome. The function should have proper error handling and be tested with unittest
def is_palindrome(word: str):
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
  def temp(*args, **kwargs):
      start = time.time()
      print(start)
      res = function(*args, **kwargs)
      final = time.time() - start
      print(final)
      print(f"El tiempo de ejecucución fue: {final}")
      return res
  return temp

@func_timer
def order(lst: list):
  lst.sort()
  return lst