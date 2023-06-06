from datetime import datetime

# Write a Python class called BankAccount with methods for depositing, withdrawing, and checking the account balance.

class BankAccount:
  __historial = {}
  funds = 0
  def __init__(self):
    self.__historial = {
      'deposit': [],
      'withdraw': [],
      'incomes': 0,
      'expenses': 0,
      'balance': 0,
    }

  def depositing(self, deposit):
    '''
      Generates an increment in user funds.

      Is meant to add the amount the user deposit in funds and saves the history of deposits in '__historial' hidden attribute.
      __________________________________________________________________________________________
      parameters:
        deposit:
          The amount user want to save in funds attribute.
      __________________________________________________________________________________________
      example:
        <instance>.depositing(100)
    '''
    if deposit < 10:
      return f"Deposits must be higher than 10 USD"
    self.funds += deposit
    self.__historial['incomes'] += deposit
    self.__historial.get('deposit').append({ 'value': deposit, 'date': str(datetime.now()) })
    return f"Your remaining funds are: {self.funds}"

  def withdrawing(self, withdraw):
    '''
      Generates a loss in user funds.

      Is meant to reduce the amount the user withdraw in funds and saves the history of deposits in '__historial' hidden attribute.
      Te max amount permitted to withdraw is 10 usd. It is impossible to take more than user have in his funds.
      __________________________________________________________________________________________
      parameters:
        withdraw:
          The amount user want to take from funds attribute.
      __________________________________________________________________________________________
      example:
        <instance>.withdrawing(100)
    '''
    if withdraw > self.funds:
      return f"Insuficient funds"
    if withdraw < 10:
      return f"Withdraws must be higher than 10 USD"
    self.funds -= withdraw
    self.__historial['expenses'] += withdraw
    self.__historial.get('withdraw').append({ 'value': withdraw, 'date': str(datetime.now()) })
    return f"Your remaining funds are: {self.funds}"

  def checking(self):
    '''
      Generates a balance of user movements.

      Is meant to generate a balance from all user movements.
      __________________________________________________________________________________________
      parameters:
        none
      __________________________________________________________________________________________
      example:
        <instance>.checking()
    '''
    self.__historial['balance'] = self.__historial['incomes'] - self.__historial['expenses']
    return f"Your balance is: {self.__historial}"

# Create a Python program that reads a text file and counts the occurrences of each word using a dictionary. The program should print the words and their counts.

def words_cleaner(txt):
  '''
    Function created only for clean data from the text file readed in function 'read_file'.

    In order to give clean data to the function 'words_counter' this function is deleting all the commas, points and remaining punctuation marks in words after split them by the spaces between.
    _____________________________________________________________________
    parameters:
      file:
        The txt file route user want to check

    example:
      words_cleaner('./file.txt')
  '''
  char = ['.', ',', ';', ':']
  with open(txt, 'r') as file:
    text = file.read()
  text = text.lower()
  words = text.split(' ')
  for i in words:
    if i[-1] in char:
      words[words.index(i)] = i[:-1]
    if '\n' in i:
      n = i.split('\n')
      if '' in n:
        n.remove('')
      for j in n:
        words.insert(words.index(i), j)
      words.pop(words.index(i))
  words_counter(words)

def words_counter(words):
  '''
      Counts the ocurrences of each word in a list of words.

      This functions was created to be called by 'words_cleaner' function but it can take parameters by itself.
      ________________________________________________________________________________
      parameters:
        words:
          A list of the words in the text user want to check.
      ________________________________________________________________________________
      Examples:
        words_counter(['time', 'to', 'sleep', 'to', 'get', 'up', 'early'])

  '''
  wset = set(words)
  counter = {}

  for word in wset:
    for wrd_text in words:
      if word == wrd_text:
        if counter.get(word):
          counter[word] += 1
        else:
          counter.update({ word: 1 })

  # print(counter)
  a = list(counter.keys())
  s = list(counter.values())
  for x in range(0, len(a)):
    print(f"{a[x]}: {s[x]}")
