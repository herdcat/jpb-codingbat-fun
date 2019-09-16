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

    def test_common_end(self):
        tests = {
            'test0' : ([0, 1, 2], [0, 1, 2], True),
            'test1' : ([0, 1, 2], [0, 1, 3], True),
            'test2' : ([0, 1, 2], [1, 1, 2], True),
            'test3' : ([1, 1, 2], [0, 1, 0], False),
            'test4' : ([1, 2, 3], [2, 3, 4], False),
            'test5' : (['a', 'b, c'], ['c', 'b', 'a'], False)
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().common_end(test[0], test[1]),test[2])

    def test_sum3(self):
        tests = {
            'test0' : ([0, 1, 2], 3),
            'test1' : ([1, 2, 3], 6),
            'test2' : ([2, 3, 4], 9),
            'test3' : ([3, 4, 5], 12),
            'test4' : ([4, 5, 6], 15),
            'test5' : ([5, 6, 7], 18),
            'test6' : ([6, 7, 8], 21),
            'test7' : ([7, 8, 9], 24),
            'test8' : ([8, 9, 10], 27),
            'test9' : ([9, 10, 11], 30)
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().sum3(test[0]),test[1])

    def test_rotate_left3(self):
        tests = {
            'test0' : ([0, 1, 2], [1, 2, 0]),
            'test1' : ([1, 2, 3], [2, 3, 1]),
            'test2' : ([2, 3, 4], [3, 4, 2]),
            'test3' : ([3, 4, 5], [4, 5, 3]),
            'test4' : ([4, 5, 6], [5, 6, 4]),
            'test5' : ([5, 6, 7], [6, 7, 5]),
            'test6' : ([6, 7, 8], [7, 8, 6]),
            'test7' : ([7, 8, 9], [8, 9, 7]),
            'test8' : ([8, 9, 10], [9, 10, 8]),
            'test9' : ([9, 10, 11], [10, 11, 9])
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().rotate_left3(test[0]),test[1])