# Write a Python program that prints the first 10 Fibonacci numbers using a loop.

def fibo():
  n = 10
  # n = input('Ingrese la cantidad de datos a imprimir: ')

  # try:
  #   n = int(n)
  # except ValueError:
  #   print('Inserta solo valores numericos, un solo numero porfavor.')
  #   return fibo()

  res = 0
  last = 0
  for i in range(0, n):
    if i <= 1:
      res = 1
      last = res
      print(res)
    else:
      temp = res
      res = res + last
      last = temp
      print(res)


# Create a Python program that checks if a given number is prime or not. The user should input a number, and the program should print whether it is prime or not.

def prime():
  n = input('Type the number you want to check: ')

  try:
    n = int(n)
  except ValueError:
    print('Inserta solo valores numericos, un solo numero porfavor.')
    return prime()

  f = ''
  for i in range(2, int(n/2) + 1):
    if n % i == 0:
      f = True

  if f:
    print(f'The number {n} is not prime')
  else:
    print(f'The number {n} is prime')