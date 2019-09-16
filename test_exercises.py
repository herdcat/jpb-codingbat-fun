import unittest
import Codingbat

class TestMyTestCases(unittest.TestCase):

    def setUp(self):
        self.cb_solutions = Codingbat.Solutions

    def test_first_last6(self):
        tests = {
            'test0' : ([6, 4, 5, 6],True),
            'test1' : ([6, 4, 5], True),
            'test2' : ([4, 5, 6], True),
            'test3' : ([4, 5], False),
            'test4' : ([5, 4], False),
            'test5' : ([5, 6, 7], False),
            'test6' : ([6, 7, 8, 9], True),
            'test7' : ([3, 4, 5, 6], True),
            'test8' : ([6, 0, 9, 6], True),
            'test9' : ([9, 8, 7], False)
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().first_last6(test[0]),test[1])

    def test_same_first_last(self):
        tests = {
            'test0' : ([0, 1, 0],True),
            'test1' : ([0, 1, 2], False),
            'test2' : (['a', 'b', 'a'], True),
            'test3' : (['a', 'b'], False),
            'test4' : ([{'a' : 0}, {'a' : 0}], True),
            'test5' : ([{'a' : 0}, {'a' : 1}], False),
            'test6' : ([[0, 1],[0, 1]], True),
            'test7' : ([[0, 1],[1, 2]], False),
            'test8' : ([0.1, 0.2, 0.1], True),
            'test9' : ([0.1, 0.2, 0.2], False)
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().same_first_last(test[0]),test[1])

    def test_make_pi(self):
        self.assertEqual(self.cb_solutions().make_pi(),[3, 1, 4])