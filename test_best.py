import unittest
from Topics.best_practices import is_palindrome


class TestBestPractice(unittest.TestCase):
  def test_wordTreatment(self):
    word = 'arenera'
    result = is_palindrome(word)
    self.assertEqual(result, f'The word "{word}" is palindrome')

    word = 'delicado'
    result = is_palindrome(word)
    self.assertEqual(result, f'The word "{word}" is not palindrome')

if __name__ == "__main__":
  unittest.main()