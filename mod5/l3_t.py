import unittest
from l3 import BlockErrors

class Tests(unittest.TestCase):
    def ignore_specific_exception(self):
        err_types = {ZeroDivisionError}
        with BlockErrors(err_types):
            a = 1 / 0
        self.assertTrue(True) 

    def propagate_unexpected_exception(self):
        err_types = {ZeroDivisionError}
        with self.assertRaises(TypeError):
            with BlockErrors(err_types):
                a = 1 / '0'  

    def inner_block_ignore_outer(self):
        outer_err_types = {TypeError}
        with BlockErrors(outer_err_types):
            inner_err_types = {ZeroDivisionError}
            with BlockErrors(inner_err_types):
                a = 1 / '0'  
            self.assertTrue(True)  
        self.assertTrue(True)  

    def ignore_child_exceptions(self):
        err_types = {TypeError}
        with BlockErrors(err_types):
            a = 1 / '0' 
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
