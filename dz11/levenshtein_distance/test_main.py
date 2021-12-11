"""" module for testing """

import unittest
from main import levenshtein_distance


class TestLevenshteinDistance(unittest.TestCase):

    """ test Levenshtein function """

    def test_identical_words(self):
        """ for identical words """
        res = levenshtein_distance("word", "word")
        self.assertEqual(res, 0)

    def test_same_length_words(self):
        """ for same length words """
        res = levenshtein_distance("mew", "new")
        self.assertEqual(res, 1)

    def test_different_words(self):
        """" for different words """
        res = levenshtein_distance("next", "exit")
        self.assertEqual(res, 2)

    def test_two_empty_words(self):
        """ for two empty words """
        res = levenshtein_distance("", "")
        self.assertEqual(res, 0)

    def test_one_empty_word(self):
        """ for one empty word """
        word = "technopark"
        self.assertEqual(len(word), levenshtein_distance("", word))


if __name__ == '__main__':
    unittest.main()
