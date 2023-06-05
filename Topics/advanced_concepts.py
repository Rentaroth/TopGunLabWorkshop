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
    if deposit < 10:
      return f"Deposits must be higher than 10 USD"
    self.funds += deposit
    self.__historial['incomes'] += deposit
    self.__historial.get('deposit').append({ 'value': deposit, 'date': str(datetime.now()) })
    return f"Your remaining funds are: {self.funds}"

  def withdrawing(self, withdraw):
    if withdraw > self.funds:
      return f"Insuficient funds"
    if withdraw < 10:
      return f"Withdraws must be higher than 10 USD"
    self.funds -= withdraw
    self.__historial['expenses'] += withdraw
    self.__historial.get('withdraw').append({ 'value': withdraw, 'date': str(datetime.now()) })
    return f"Your remaining funds are: {self.funds}"

  def checking(self):
    self.__historial['balance'] = self.__historial['incomes'] - self.__historial['expenses']
    return f"Your balance is: {self.__historial}"

# Create a Python program that reads a text file and counts the occurrences of each word using a dictionary. The program should print the words and their counts.

def read_file(txt):
  with open(txt, 'r') as file:
    return file.read()

char = ['.', ',', ';', ':']
def words_cleaner(file):
  text = read_file(file)
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
  ws = set(words)
  words_counter(ws, words)

def words_counter(wset, words):
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
