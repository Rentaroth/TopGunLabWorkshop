import os, gc

# Write a Python program that takes two numbers as input from the user and prints their sum.
def __isInteger(num):
  if num >= 1:
    return __isInteger(num-1)
  elif num == 0:
    return True
  else:
    return False

def sum():
  num_1 = input('Insert a number: ')
  num_2 = input('Insert a number again: ')

  try:
    num_1 = float(num_1)
    num_2 = float(num_2)
  except ValueError:
    # os.system('clear')
    print('Ingresa un valor numérico.')
    return sum()
  
  res = num_1 + num_2
  if __isInteger(res):
    return int(res)
  else:
    return res
  

# a = sum()
# print(a)

# Create a Python program that converts a temperature from Fahrenheit to Celsius. The user should enter the temperature in Fahrenheit, and the program should print the equivalent temperature in Celsius.

def toCelcius():
  far = input('Insert the temperature in Farenheit: ')
  try:
    far = float(far)
  except ValueError:
    # Este feature es para borrar la terminal en caso de error, pero solo sirve con terminal Bash
    # os.system('clear')
    print('Ingresa un valor numérico equivalente a la temperatura en Farenheit.')
    return toCelcius()
  
  res = (far - 32)*(5/9)
  return f'la temperatura en Celcius es: {res}'