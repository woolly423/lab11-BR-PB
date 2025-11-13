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

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 5), 10)
        self.assertEqual(mul(-2, 3), -6)
        self.assertAlmostEqual(mul(0.1, 0.2), 0.02)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(10, 2), 5)
        self.assertAlmostEqual(div(1, 3), 1 / 3)
    ##########################

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
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(1, 10)
        with self.assertRaises(ValueError):
            log(-2, 10)
        with self.assertRaises(ValueError):
            log(2, -5)
        with self.assertRaises(ValueError):
            log(2, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(math.hypot(3, 4), 5.0)
        self.assertAlmostEqual(math.hypot(-8, 15), 17.0)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(2), math.sqrt(2), places=7)
        with self.assertRaises(ValueError):
            square_root(-1)
    #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()