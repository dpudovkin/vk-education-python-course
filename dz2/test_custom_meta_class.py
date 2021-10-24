"""" Module for test custom meta class """
import unittest
from faker import Faker
from custom_meta_class import CustomMeta


class TestCustomMetaClass(unittest.TestCase):
    """" TestCustomMetaClass """

    def setUp(self):
        """" setUp function """
        self.fake = Faker()
        self.attr_name = "name"

    def test_class_attr(self):
        """" test class attribute function """
        attr_value = self.fake.name()
        CustomClass = CustomMeta("TestCustomClass", (object,), {self.attr_name: attr_value})
        assert CustomClass.__dict__[f'custom_{self.attr_name}'] == attr_value

    def test_obj_attr(self):
        """" test object attribute function """
        attr_value = self.fake.name()
        CustomClass = CustomMeta("TestCustomClass", (object,), {self.attr_name: attr_value})
        instance = CustomClass()
        instance.attr = attr_value
        assert instance.__dict__["custom_attr"] == attr_value

    def test_class_method(self):
        """" test class method function """
        attr_value = self.fake.name()

        @staticmethod
        def get():
            return attr_value

        CustomClass = CustomMeta("TestCustomClass", (object,), {'get': get})
        assert CustomClass.custom_get() == attr_value

    def test_obj_method(self):
        """" test object method function """
        attr_value = self.fake.name()

        def get(_):
            return attr_value

        CustomClass = CustomMeta("TestCustomClass", (object,), {'get': get})
        instance = CustomClass()
        assert instance.custom_get() == attr_value
