import unittest
from datetime import datetime
from person import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person("John Doe", 1990)

    def get_age(self):
        current_year = datetime.now().year
        self.assertEqual(self.person.get_age(), current_year - 1990)

    def get_name(self):
        self.assertEqual(self.person.get_name(), "John Doe")

    def set_name(self):
        self.person.set_name("Jane Doe")
        self.assertEqual(self.person.get_name(), "Jane Doe")

    def set_address(self):
        self.person.set_address("123 Main St")
        self.assertEqual(self.person.get_address(), "123 Main St")

    def get_address(self):
        self.person.set_address("123 Main St")
        self.assertEqual(self.person.get_address(), "123 Main St")

    def is_homeless(self):
        self.assertTrue(self.person.is_homeless())
        self.person.set_address("123 Main St")
        self.assertFalse(self.person.is_homeless())


if __name__ == '__main__':
    unittest.main()