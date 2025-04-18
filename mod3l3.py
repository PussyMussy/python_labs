import unittest
import json
import copy
from mod2 import l7

class TestAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = l7.app.test_client()
        cls.app.testing = True
        cls.app.application.storage = {
            2023: {
                1: 1000,
                2: 500
            }
        }

    def add_expense_valid(self):
        response = self.app.post('/add/20230101/200')
        self.assertEqual(response.status_code, 201)
        self.assertIn("Expense added successfully".encode('utf-8'), response.data)

    def add_expense_increases_total(self):
        self.app.post('/add/20230101/200')
        response = self.app.get('/calculate/2023/1')
        data = json.loads(response.data)
        self.assertEqual(data['total_expense'], 1200)

    def add_invalid_date_format(self):
        response = self.app.post('/add/2023-01-01/200')
        self.assertIn("Invalid date format. Use YYYYMMDD.".encode('utf-8'), response.data)

class TestYear(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = l7.app.test_client()
        cls.app.testing = True
        cls.app.application.storage = {
            2023: {
                1: 1000,
                2: 500
            }
        }

    def calculate_year_valid(self):
        response = self.app.get('/calculate/2023')
        data = json.loads(response.data)
        self.assertEqual(data['total_expense'], 1500)

    def calculate_year_no_data(self):
        temp_storage = copy.deepcopy(self.app.application.storage)
        self.app.application.storage.clear()
        response = self.app.get('/calculate/2023')
        data = json.loads(response.data)
        self.assertEqual(data['total_expense'], 0)
        self.app.application.storage = temp_storage

    def calculate_year_nonexistent(self):
        response = self.app.get('/calculate/2024')
        data = json.loads(response.data)
        self.assertEqual(data['total_expense'], 0)

class TestMonth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = l7.app.test_client()
        cls.app.testing = True
        cls.app.application.storage = {
            2023: {
                1: 1000,
                2: 500
            }
        }

    def calculate_month_valid(self):
        response = self.app.get('/calculate/2023/2')
        data = json.loads(response.data)
        self.assertEqual(data['total_expense'], 500)

    def calculate_month_no_data(self):
        temp_storage = copy.deepcopy(self.app.application.storage)
        self.app.application.storage.clear()
        response = self.app.get('/calculate/2023/1')
        data = json.loads(response.data)
        self.assertEqual(data['total_expense'], 0)
        self.app.application.storage = temp_storage

    def calculate_month_nonexistent(self):
        response = self.app.get('/calculate/2023/3')
        data = json.loads(response.data)
        self.assertEqual(data['total_expense'], 0)

if __name__ == '__main__':
    unittest.main()