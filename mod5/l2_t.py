import unittest
from l2 import app
import l2

class TaskTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        l2.app.config['WTF_CSRF_ENABLED'] = False

    def timeout_exceeded(self):
        response = self.app.post('/execute', data={'code': 'import time; time.sleep(5)', 'timeout': 1})
        self.assertEqual(response.status_code, 408)
        self.assertIn('Execution timed out', response.get_data(as_text=True))

    def invalid_input(self):
        response = self.app.post('/execute', data={'code': '', 'timeout': 1})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid input', response.get_data(as_text=True))

    def safe_code_execution(self):
        response = self.app.post('/execute', data={'code': 'print("Hello")', 'timeout': 1})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello', response.get_data(as_text=True))

    def unsafe_code(self):
        response = self.app.post('/execute', data={'code': 'print("Hello") shell=True', 'timeout': 1})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Unsafe code detected', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
