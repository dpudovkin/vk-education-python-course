"""" Test CustomList module """

import unittest
from custom_collections import CustomList


class TestCustomList(unittest.TestCase):
    """Test custom list class"""

    def setUp(self):
        """ setUp function """
        self.list_a = [1, 2, 3, 4, 5]
        self.list_b = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
        self.custom_list_a = CustomList(self.list_a)
        self.custom_list_b = CustomList(self.list_b)
        self.add_list = [-9, -7, -5, -3, -1, -5, -4, -3, -2, -1]
        self.sub_a_b_list = [11, 11, 11, 11, 11, 5, 4, 3, 2, 1]
        self.sub_b_a_list = [-item for item in self.sub_a_b_list]

    def test_add_custom_to_custom(self):
        """ test_add_custom_to_custom function """
        assert self.add_list == self.custom_list_b + self.custom_list_a

    def test_add_default_to_custom(self):
        """ test_add_default_to_custom function """
        assert self.add_list == self.list_a + self.custom_list_b

    def test_add_custom_to_default(self):
        """ test_add_custom_to_default function """
        assert self.add_list == self.list_b + self.custom_list_a

    def test_sub_custom_to_default(self):
        """ test_sub_custom_to_default function """
        assert self.sub_a_b_list == self.custom_list_a - self.list_b

    def test_sub_default_to_custom(self):
        """ test_sub_default_to_custom function """
        assert self.sub_b_a_list == self.list_b - self.custom_list_a

    def test_sub_custom_to_custom(self):
        """ test_sub_custom_to_custom function """
        assert self.sub_b_a_list == self.custom_list_b - self.custom_list_a

    def test_eq(self):
        """ equal test function """
        assert ((sum(self.list_a) == sum(self.list_b)) == (self.list_a == self.list_b))

    def test_ne(self):
        """ not equal test function """
        assert ((sum(self.list_a) != sum(self.list_b)) == (self.list_a != self.list_b))

    def test_gt(self):
        """ greater test function """
        assert ((sum(self.list_a) > sum(self.list_b)) == (self.list_a > self.list_b))

    def test_lt(self):
        """ less test function """
        assert ((sum(self.list_a) < sum(self.list_b)) == (self.list_a < self.list_b))

    def test_le(self):
        """ less or equal test function """
        assert ((sum(self.list_a) <= sum(self.list_b)) == (self.list_a <= self.list_b))

    def test_ge(self):
        """ greater or equal test function """
        assert ((sum(self.list_a) >= sum(self.list_b)) == (self.list_a >= self.list_b))
