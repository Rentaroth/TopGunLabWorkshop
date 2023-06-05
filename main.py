from Topics import advanced_concepts

if __name__ == "__main__":
  bank = advanced_concepts.BankAccount()

  print(bank.depositing(500))
  print(bank.withdrawing(125))
  a = bank.checking()
  print(a)

  print('\n' + '*********'*10 + '\n')
  advanced_concepts.words_cleaner('./Topics/text.txt')

  