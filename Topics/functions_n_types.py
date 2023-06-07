# Write a Python function called find_maximum that takes a list of numbers as input and returns the maximum number from the list.

def find_maximum(group: list):
  if len(group) > 1:
    if group[-1] >= group[-2]:
      group.pop(-2)
      return find_maximum(group)
    else:
      group.pop(-1)
      return find_maximum(group)
  else:
    return group[-1]


# Create a Python function called reverse_string that takes a string as input and returns the reversed string.

def reverse_string(chain: str, a = ''):
  if chain != '':
    a = a + chain[-1]
    return reverse_string(chain[:-1], a)
  else:
    return a