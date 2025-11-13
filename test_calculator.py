import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code
    def test_add(self):
        self.assertEqual(add(1,0),1)
        self.assertEqual(add(-1,1.1),0.1)
        self.assertEqual(add(66,1),67)
        
    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################
    def test_subtract(self):
        self.assertEqual(sub(1,0),1)
        self.assertEqual(sub(5.5,10),-4.5)
        self.assertEqual(sub(68,1),67)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0,67)

    # def test_logarithm(self): # 3 assertions
    #     fill in code
    def test_logarithm(self):
        self.assertEqual(log(2,8),3)
        self.assertEqual(log(4,256),4)
        self.assertEqual(log(10,100),2)

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(0,2)
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()