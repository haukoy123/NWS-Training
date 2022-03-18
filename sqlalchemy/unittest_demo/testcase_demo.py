from os import terminal_size
import unittest
import pytest
from parameterized import parameterized, parameterized_class


def div(a,b):
   return a/b




def string_to_number(a):
    return int(a)

# @parameterized_class(('a', 'b'), [
#    (50, 40),
#    (50, 50),
# ])

# @parameterized_class([
#    { "a": 3, "b": 2 },
#    { "a": 5, "b": -4 },
# ])

class suiteTest(unittest.TestCase):
    # a = 50
    # b = 30
    @pytest.fixture()
    def my_fixture():
        return 'This is some fixture data'

    def test_with_a_fixture(self, my_fixture):
         print(my_fixture)


    # def test_run_call_order__error_in_setUp(self):
    #     events = []

    #     def setUp():
    #         events.append('setUp')
    #         # raise RuntimeError('raised by setUp')

    #     def test():
    #         events.append('test')

    #     def tearDown():
    #         events.append('tearDown')

    #     expected = ['setUp', 'test', 'tearDown']
    #     t = unittest.FunctionTestCase(test, setUp, tearDown).run()
    #     self.assertEqual(events, expected)

    # def testadd(self):
    #     """Add"""
    #     result = self.a + self.b
    #     self.assertEqual(result,100)

    # @unittest.skipIf(a>b, "Skip over this routine")
    # def testsub(self):
    #     """sub"""
    #     # skipIf thay cho viec ktra dieu kien -> skiptest
    #     if self.a > self.b:
    #         self.skipTest("external resource not available")
    #     result = self.a-self.b
    #     self.assertTrue(result == -10)
    
    # @unittest.skipUnless(b == 0, "Skip over this routine")
    # def testdiv(self):
    #     """div"""
    #     result = self.a/self.b
    #     self.assertTrue(result == 1)

    # @unittest.expectedFailure
    # def testmul(self):
    #     """mul"""
    #     result = self.a*self.b
    #     self.assertEqual(result == 0)

    # def test_even(self):
    #     """
    #     Test that numbers between 0 and 5 are all even.
    #     """
    #     for i in range(0, 6):
    #         with self.subTest(i=i):
    #             self.assertEqual(i % 2, 0)


    # def testraise(self):
    #     self.assertRaises(ZeroDivisionError, div, 1,0)
    #     self.assertRaises(ValueError, string_to_number, 'd')

    # @parameterized.expand([
    #     (1, 11),
    #     (2, 22),
    #     (3, 34),
    # ])
    
    # def test_multiplication_11(self, num, output):
    #     with self.subTest(i=num):
    #         self.assertEqual(11 * num, output)


if __name__ == '__main__':
    unittest.main()