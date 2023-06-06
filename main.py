from Topics import best_practices

if __name__ == "__main__":
  s = best_practices.is_palindrome('reconocer')
  print(s)
  x = best_practices.is_palindrome('petalo')
  print(x)
  v = best_practices.is_palindrome(123)
  print(v)
  v = best_practices.is_palindrome('123')
  print(v)

  print('\n' + '*****************'*10 + '\n')

  
  k = best_practices.order([2, 4, 6, 3, 3, 65, 341342314, 12341234, 35144262346, 52354, 123453425134, 235463456, 324523462346, 8, 4, 0, 3, 4, 2])
  print(k)
