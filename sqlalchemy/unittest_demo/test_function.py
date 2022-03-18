import pytest
import unittest

# @pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_run_call_order__error_in_setUp():
        events = []

        def setUp():
            events.append('setUp')

        def test():
            events.append('test')

        def tearDown():
            events.append('tearDown')

        expected = ['setUp', 'test', 'tearDown']
        unittest.FunctionTestCase(test, setUp, tearDown).run()
        print(events)
        assert events == expected


# def setup():
#     num = 1
#     output = 2
#     return num, output


# def test_multiplication_11(num, output):
#    assert 11*num == output


t = unittest.FunctionTestCase(test_run_call_order__error_in_setUp)

unittest.TextTestRunner().run(t)