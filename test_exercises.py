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

    def test_reverse3(self):
        tests = {
            'test0' : ([0, 1, 2], [2, 1, 0]),
            'test1' : ([1, 2, 3], [3, 2, 1]),
            'test2' : ([2, 3, 4], [4, 3, 2]),
            'test3' : ([3, 4, 5], [5, 4, 3]),
            'test4' : ([4, 5, 6], [6, 5, 4]),
            'test5' : ([5, 6, 7], [7, 6, 5]),
            'test6' : ([6, 7, 8], [8, 7, 6]),
            'test7' : ([7, 8, 9], [9, 8, 7]),
            'test8' : ([8, 9, 10], [10, 9, 8]),
            'test9' : ([9, 10, 11], [11, 10, 9])
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().reverse3(test[0]),test[1])

    def test_max_end3(self):
        tests = {
            'test0' : ([1, 2, 3], [3, 3, 3]),
            'test1' : ([11, 5, 9], [11, 11, 11]),
            'test2' : ([2, 11, 3], [3, 3, 3]),
            'test3' : ([11, 3, 3], [11, 11, 11]),
            'test4' : ([3, 11, 11], [11, 11, 11]),
            'test5' : ([2, 2, 2], [2, 2, 2]),
            'test6' : ([2, 11, 2], [2, 2, 2]),
            'test7' : ([0, 0, 1], [1, 1, 1]),
            'test8' : ([8, 9, 10], [10, 10, 10]),
            'test9' : ([9, 10, 11], [11, 11, 11])
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().max_end3(test[0]),test[1])

    def test_sum2(self):
        tests = {
            'test0' : ([1, 2, 3], 3),
            'test1' : ([11, 5, 9], 16),
            'test2' : ([2, 11, 3], 13),
            'test3' : ([11, 3, 3], 14),
            'test4' : ([3, 11, 11], 14),
            'test5' : ([2, 2, 2], 4),
            'test6' : ([2, 11, 2], 13),
            'test7' : ([0, 0, 1], 0),
            'test8' : ([8, 9, 10], 17),
            'test9' : ([9, 10, 11], 19)
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().sum2(test[0]),test[1])

    def test_middle_way(self):
        tests = {
            'test0' : ([1, 2, 3], [4, 5, 6], [2, 5]),
            'test1' : ([7, 7, 7], [3, 8, 0], [7, 8]),
            'test2' : ([5, 2, 9], [1, 4, 5], [2, 4]),
            'test3' : ([1, 9, 7], [4, 8, 8], [9, 8]),
            'test4' : ([1, 2, 3], [3, 1, 4], [2, 1]),
            'test5' : ([1, 2, 3], [4, 1, 1], [2, 1]),
            'test6' : ([2, 11, 2], [5, 2, 9], [11, 2]),
            'test7' : ([0, 0, 1], [3, 8, 0], [0, 8]),
            'test8' : ([8, 9, 10], [3, 1, 4], [9, 1]),
            'test9' : ([9, 10, 11], [1, 2, 3], [10, 2])
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().middle_way(test[0],test[1]), test[2])

    def test_make_ends(self):
        tests = {
            'test0' : ([1, 2, 3], [1, 3]),
            'test1' : ([11, 5, 9], [11, 9]),
            'test2' : ([2, 11, 3], [2, 3]),
            'test3' : ([11, 3, 3], [11, 3]),
            'test4' : ([3, 11, 11], [3, 11]),
            'test5' : ([2, 2, 2], [2, 2]),
            'test6' : ([2, 11, 2], [2, 2]),
            'test7' : ([0, 0, 1], [0, 1]),
            'test8' : ([8, 9, 10], [8, 10]),
            'test9' : ([9, 10, 11], [9, 11])
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().make_ends(test[0]),test[1])

    def test_has23(self):
        tests = {
            'test0' : ([2, 5], True),
            'test1' : ([4, 3], True),
            'test2' : ([4, 5], False),
            'test3' : ([2, 2], True),
            'test4' : ([3, 2], True),
            'test5' : ([3, 3], True),
            'test6' : ([7, 7], False),
            'test7' : ([3, 9], True),
            'test8' : ([9, 5], False),
            'test9' : ([3, 5], True)
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().has23(test[0]),test[1])

    def test_count_evens(self):
        tests = {
            'test0' : ([0, 1, 2], 2),
            'test1' : ([1, 2, 3], 1),
            'test2' : ([2, 3, 4], 2),
            'test3' : ([2, 4, 6, 8], 4),
            'test4' : ([1, 3, 5, 7], 0),
            'test5' : ([3, 1, 4], 1),
            'test6' : ([1, 7, 2], 1),
            'test7' : ([8, 6, 7], 2),
            'test8' : ([5, 3], 0),
            'test9' : ([0, 9], 1)
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().count_evens(test[0]),test[1])

    def test_big_diff(self):
        tests = {
            'test0' : ([0, 1, 2], 2),
            'test1' : ([1, 2, 3], 2),
            'test2' : ([2, 3, 4], 2),
            'test3' : ([2, 4, 6, 8], 6),
            'test4' : ([1, 3, 5, 7], 6),
            'test5' : ([3, 1, 4], 3),
            'test6' : ([1, 7, 2], 6),
            'test7' : ([8, 6, 7], 2),
            'test8' : ([5, 3], 2),
            'test9' : ([0, 9], 9)
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().big_diff(test[0]),test[1])

    def test_centered_average(self):
        # tests = {
        #     'test0' : ([0, 1, 2], 2),
        #     'test1' : ([1, 2, 3], 2),
        #     'test2' : ([2, 3, 4], 2),
        #     'test3' : ([2, 4, 6, 8], 6),
        #     'test4' : ([1, 3, 5, 7], 6),
        #     'test5' : ([3, 1, 4], 3),
        #     'test6' : ([1, 7, 2], 6),
        #     'test7' : ([8, 6, 7], 2),
        #     'test8' : ([5, 3], 2),
        #     'test9' : ([0, 9], 9)
        # }
        # for test in tests.values():
        #     self.assertEqual(self.cb_solutions().centered_average(test[0]),test[1])
        self.assertTrue(True)

    def test_sum13(self):
        # tests = {
        #     'test0' : ([0, 1, 2], 2),
        #     'test1' : ([1, 2, 3], 2),
        #     'test2' : ([2, 3, 4], 2),
        #     'test3' : ([2, 4, 6, 8], 6),
        #     'test4' : ([1, 3, 5, 7], 6),
        #     'test5' : ([3, 1, 4], 3),
        #     'test6' : ([1, 7, 2], 6),
        #     'test7' : ([8, 6, 7], 2),
        #     'test8' : ([5, 3], 2),
        #     'test9' : ([0, 9], 9)
        # }
        # for test in tests.values():
        #     self.assertEqual(self.cb_solutions().sum13(test[0]),test[1])
        self.assertTrue(True)

    def test_ex5(self):
        self.assertTrue(True)

    def test_has22(self):
        # tests = {
        #     'test0' : ([0, 1, 2], 2),
        #     'test1' : ([1, 2, 3], 2),
        #     'test2' : ([2, 3, 4], 2),
        #     'test3' : ([2, 4, 6, 8], 6),
        #     'test4' : ([1, 3, 5, 7], 6),
        #     'test5' : ([3, 1, 4], 3),
        #     'test6' : ([1, 7, 2], 6),
        #     'test7' : ([8, 6, 7], 2),
        #     'test8' : ([5, 3], 2),
        #     'test9' : ([0, 9], 9)
        # }
        # for test in tests.values():
        #     self.assertEqual(self.cb_solutions().has22(test[0]),test[1])
        self.assertTrue(True)

    def test_cigar_party(self):
        # tests = {
        #     'test0' : ([0, 1, 2], 2),
        #     'test1' : ([1, 2, 3], 2),
        #     'test2' : ([2, 3, 4], 2),
        #     'test3' : ([2, 4, 6, 8], 6),
        #     'test4' : ([1, 3, 5, 7], 6),
        #     'test5' : ([3, 1, 4], 3),
        #     'test6' : ([1, 7, 2], 6),
        #     'test7' : ([8, 6, 7], 2),
        #     'test8' : ([5, 3], 2),
        #     'test9' : ([0, 9], 9)
        # }
        # for test in tests.values():
        #     self.assertEqual(self.cb_solutions().cigar_party(test[0]),test[1])
        self.assertTrue(True)

    def test_date_fashion(self):
        # tests = {
        #     'test0' : ([0, 1, 2], 2),
        #     'test1' : ([1, 2, 3], 2),
        #     'test2' : ([2, 3, 4], 2),
        #     'test3' : ([2, 4, 6, 8], 6),
        #     'test4' : ([1, 3, 5, 7], 6),
        #     'test5' : ([3, 1, 4], 3),
        #     'test6' : ([1, 7, 2], 6),
        #     'test7' : ([8, 6, 7], 2),
        #     'test8' : ([5, 3], 2),
        #     'test9' : ([0, 9], 9)
        # }
        # for test in tests.values():
        #     self.assertEqual(self.cb_solutions().date_fashion(test[0]),test[1])
        self.assertTrue(True)

    def test_squirrel_play(self):
        # tests = {
        #     'test0' : ([0, 1, 2], 2),
        #     'test1' : ([1, 2, 3], 2),
        #     'test2' : ([2, 3, 4], 2),
        #     'test3' : ([2, 4, 6, 8], 6),
        #     'test4' : ([1, 3, 5, 7], 6),
        #     'test5' : ([3, 1, 4], 3),
        #     'test6' : ([1, 7, 2], 6),
        #     'test7' : ([8, 6, 7], 2),
        #     'test8' : ([5, 3], 2),
        #     'test9' : ([0, 9], 9)
        # }
        # for test in tests.values():
        #     self.assertEqual(self.cb_solutions().squirrel_play(test[0]),test[1])
        self.assertTrue(True)

    def test_caught_speeding(self):
        # tests = {
        #     'test0' : ([0, 1, 2], 2),
        #     'test1' : ([1, 2, 3], 2),
        #     'test2' : ([2, 3, 4], 2),
        #     'test3' : ([2, 4, 6, 8], 6),
        #     'test4' : ([1, 3, 5, 7], 6),
        #     'test5' : ([3, 1, 4], 3),
        #     'test6' : ([1, 7, 2], 6),
        #     'test7' : ([8, 6, 7], 2),
        #     'test8' : ([5, 3], 2),
        #     'test9' : ([0, 9], 9)
        # }
        # for test in tests.values():
        #     self.assertEqual(self.cb_solutions().caught_speeding(test[0]),test[1])
        self.assertTrue(True)

    def test_sorta_sum(self):
        # tests = {
        #     'test0' : ([0, 1, 2], 2),
        #     'test1' : ([1, 2, 3], 2),
        #     'test2' : ([2, 3, 4], 2),
        #     'test3' : ([2, 4, 6, 8], 6),
        #     'test4' : ([1, 3, 5, 7], 6),
        #     'test5' : ([3, 1, 4], 3),
        #     'test6' : ([1, 7, 2], 6),
        #     'test7' : ([8, 6, 7], 2),
        #     'test8' : ([5, 3], 2),
        #     'test9' : ([0, 9], 9)
        # }
        # for test in tests.values():
        #     self.assertEqual(self.cb_solutions().sorta_sum(test[0]),test[1])
        self.assertTrue(True)

    def test_alarm_clock(self):
        # tests = {
        #     'test0' : ([0, 1, 2], 2),
        #     'test1' : ([1, 2, 3], 2),
        #     'test2' : ([2, 3, 4], 2),
        #     'test3' : ([2, 4, 6, 8], 6),
        #     'test4' : ([1, 3, 5, 7], 6),
        #     'test5' : ([3, 1, 4], 3),
        #     'test6' : ([1, 7, 2], 6),
        #     'test7' : ([8, 6, 7], 2),
        #     'test8' : ([5, 3], 2),
        #     'test9' : ([0, 9], 9)
        # }
        # for test in tests.values():
        #     self.assertEqual(self.cb_solutions().alarm_clock(test[0]),test[1])
        self.assertTrue(True)

    def test_love6(self):
        # tests = {
        #     'test0' : ([0, 1, 2], 2),
        #     'test1' : ([1, 2, 3], 2),
        #     'test2' : ([2, 3, 4], 2),
        #     'test3' : ([2, 4, 6, 8], 6),
        #     'test4' : ([1, 3, 5, 7], 6),
        #     'test5' : ([3, 1, 4], 3),
        #     'test6' : ([1, 7, 2], 6),
        #     'test7' : ([8, 6, 7], 2),
        #     'test8' : ([5, 3], 2),
        #     'test9' : ([0, 9], 9)
        # }
        # for test in tests.values():
        #     self.assertEqual(self.cb_solutions().love6(test[0]),test[1])
        self.assertTrue(True)

    def test_in1to10(self):
        # tests = {
        #     'test0' : ([0, 1, 2], 2),
        #     'test1' : ([1, 2, 3], 2),
        #     'test2' : ([2, 3, 4], 2),
        #     'test3' : ([2, 4, 6, 8], 6),
        #     'test4' : ([1, 3, 5, 7], 6),
        #     'test5' : ([3, 1, 4], 3),
        #     'test6' : ([1, 7, 2], 6),
        #     'test7' : ([8, 6, 7], 2),
        #     'test8' : ([5, 3], 2),
        #     'test9' : ([0, 9], 9)
        # }
        # for test in tests.values():
        #     self.assertEqual(self.cb_solutions().in1to10(test[0]),test[1])
        self.assertTrue(True)

    def test_near_ten(self):
        # tests = {
        #     'test0' : ([0, 1, 2], 2),
        #     'test1' : ([1, 2, 3], 2),
        #     'test2' : ([2, 3, 4], 2),
        #     'test3' : ([2, 4, 6, 8], 6),
        #     'test4' : ([1, 3, 5, 7], 6),
        #     'test5' : ([3, 1, 4], 3),
        #     'test6' : ([1, 7, 2], 6),
        #     'test7' : ([8, 6, 7], 2),
        #     'test8' : ([5, 3], 2),
        #     'test9' : ([0, 9], 9)
        # }
        # for test in tests.values():
        #     self.assertEqual(self.cb_solutions().near_ten(test[0]),test[1])
        self.assertTrue(True)

    def test_make_bricks(self):
        # tests = {
        #     'test0' : ([0, 1, 2], 2),
        #     'test1' : ([1, 2, 3], 2),
        #     'test2' : ([2, 3, 4], 2),
        #     'test3' : ([2, 4, 6, 8], 6),
        #     'test4' : ([1, 3, 5, 7], 6),
        #     'test5' : ([3, 1, 4], 3),
        #     'test6' : ([1, 7, 2], 6),
        #     'test7' : ([8, 6, 7], 2),
        #     'test8' : ([5, 3], 2),
        #     'test9' : ([0, 9], 9)
        # }
        # for test in tests.values():
        #     self.assertEqual(self.cb_solutions().make_bricks(test[0]),test[1])
        self.assertTrue(True)

    def test_lone_sum(self):
        # tests = {
        #     'test0' : ([0, 1, 2], 2),
        #     'test1' : ([1, 2, 3], 2),
        #     'test2' : ([2, 3, 4], 2),
        #     'test3' : ([2, 4, 6, 8], 6),
        #     'test4' : ([1, 3, 5, 7], 6),
        #     'test5' : ([3, 1, 4], 3),
        #     'test6' : ([1, 7, 2], 6),
        #     'test7' : ([8, 6, 7], 2),
        #     'test8' : ([5, 3], 2),
        #     'test9' : ([0, 9], 9)
        # }
        # for test in tests.values():
        #     self.assertEqual(self.cb_solutions().lone_sum(test[0]),test[1])
        self.assertTrue(True)

    def test_lucky_sum(self):
        # tests = {
        #     'test0' : ([0, 1, 2], 2),
        #     'test1' : ([1, 2, 3], 2),
        #     'test2' : ([2, 3, 4], 2),
        #     'test3' : ([2, 4, 6, 8], 6),
        #     'test4' : ([1, 3, 5, 7], 6),
        #     'test5' : ([3, 1, 4], 3),
        #     'test6' : ([1, 7, 2], 6),
        #     'test7' : ([8, 6, 7], 2),
        #     'test8' : ([5, 3], 2),
        #     'test9' : ([0, 9], 9)
        # }
        # for test in tests.values():
        #     self.assertEqual(self.cb_solutions().lucky_sum(test[0]),test[1])
        self.assertTrue(True)

    def test_no_teen_sum(self):
        # tests = {
        #     'test0' : ([0, 1, 2], 2),
        #     'test1' : ([1, 2, 3], 2),
        #     'test2' : ([2, 3, 4], 2),
        #     'test3' : ([2, 4, 6, 8], 6),
        #     'test4' : ([1, 3, 5, 7], 6),
        #     'test5' : ([3, 1, 4], 3),
        #     'test6' : ([1, 7, 2], 6),
        #     'test7' : ([8, 6, 7], 2),
        #     'test8' : ([5, 3], 2),
        #     'test9' : ([0, 9], 9)
        # }
        # for test in tests.values():
        #     self.assertEqual(self.cb_solutions().no_teen_sum(test[0]),test[1])
        self.assertTrue(True)

    def test_round_sum(self):
        # tests = {
        #     'test0' : ([0, 1, 2], 2),
        #     'test1' : ([1, 2, 3], 2),
        #     'test2' : ([2, 3, 4], 2),
        #     'test3' : ([2, 4, 6, 8], 6),
        #     'test4' : ([1, 3, 5, 7], 6),
        #     'test5' : ([3, 1, 4], 3),
        #     'test6' : ([1, 7, 2], 6),
        #     'test7' : ([8, 6, 7], 2),
        #     'test8' : ([5, 3], 2),
        #     'test9' : ([0, 9], 9)
        # }
        # for test in tests.values():
        #     self.assertEqual(self.cb_solutions().round_sum(test[0]),test[1])
        self.assertTrue(True)

    def test_close_far(self):
        # tests = {
        #     'test0' : ([0, 1, 2], 2),
        #     'test1' : ([1, 2, 3], 2),
        #     'test2' : ([2, 3, 4], 2),
        #     'test3' : ([2, 4, 6, 8], 6),
        #     'test4' : ([1, 3, 5, 7], 6),
        #     'test5' : ([3, 1, 4], 3),
        #     'test6' : ([1, 7, 2], 6),
        #     'test7' : ([8, 6, 7], 2),
        #     'test8' : ([5, 3], 2),
        #     'test9' : ([0, 9], 9)
        # }
        # for test in tests.values():
        #     self.assertEqual(self.cb_solutions().close_far(test[0]),test[1])
        self.assertTrue(True)

    def test_make_chocolate(self):
        # tests = {
        #     'test0' : ([0, 1, 2], 2),
        #     'test1' : ([1, 2, 3], 2),
        #     'test2' : ([2, 3, 4], 2),
        #     'test3' : ([2, 4, 6, 8], 6),
        #     'test4' : ([1, 3, 5, 7], 6),
        #     'test5' : ([3, 1, 4], 3),
        #     'test6' : ([1, 7, 2], 6),
        #     'test7' : ([8, 6, 7], 2),
        #     'test8' : ([5, 3], 2),
        #     'test9' : ([0, 9], 9)
        # }
        # for test in tests.values():
        #     self.assertEqual(self.cb_solutions().make_chocolate(test[0]),test[1])
        self.assertTrue(True)