import unittest
from main import levenshtein_distance


class TestLevenshteinDistance(unittest.TestCase):

    def test_equal_word(self):
        res = levenshtein_distance("word", "word")
        self.assertEqual(res, 0)

    def test_equal_length_words(self):
        res = levenshtein_distance("ward", "word")
        self.assertEqual(res, 1)


if __name__ == '__main__':
    unittest.main()