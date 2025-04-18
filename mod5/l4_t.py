import unittest
import io
import sys
from l4 import Redirect

class TestRedirect(unittest.TestCase):
    def redirect_stdout_and_stderr(self):
        stdout_buffer = io.StringIO()
        stderr_buffer = io.StringIO()

        with Redirect(stdout=stdout_buffer, stderr=stderr_buffer):
            print('Test stdout')
            print('Test stderr', file=sys.stderr)

        self.assertEqual(stdout_buffer.getvalue(), 'Test stdout\n')
        self.assertIn('Test stderr', stderr_buffer.getvalue())

    def redirect_only_stdout(self):
        stdout_buffer = io.StringIO()

        with Redirect(stdout=stdout_buffer):
            print('Only stdout test')

        self.assertEqual(stdout_buffer.getvalue(), 'Only stdout test\n')

    def redirect_only_stderr(self):
        stderr_buffer = io.StringIO()

        with Redirect(stderr=stderr_buffer):
            print('Only stderr test', file=sys.stderr)

        self.assertIn('Only stderr test', stderr_buffer.getvalue())

if __name__ == '__main__':
    unittest.main()
