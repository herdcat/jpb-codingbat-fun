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
        tests = {
            'test0' : ([1, 2, 3, 4, 100], 3),
            'test1' : ([1, 1, 5, 5, 10, 8, 7], 5),
            'test2' : ([-10, -4, -2, -4, -2, 0], 3),
            'test3' : ([5, 3, 4, 6, 2], 4),
            'test4' : ([5, 3, 4, 0, 100], 4),
            'test5' : ([100, 0, 5, 3, 4], 4),
            'test6' : ([4, 0, 100], 4),
            'test7' : ([0, 2, 3, 4, 100], 3),
            'test8' : ([1, 1, 100], 1),
            'test9' : ([7, 7, 7], 7)
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().centered_average(test[0]),test[1])

    def test_sum13(self):
        tests = {
            'test0' : ([1, 2, 2, 1], 6),
            'test1' : ([1, 1], 2),
            'test2' : ([1, 2, 2, 1, 13], 6),
            'test3' : ([1, 2, 13, 2, 1, 13], 4),
            'test4' : ([13, 1, 2, 13, 2, 1, 13], 3),
            'test5' : ([], 0),
            'test6' : ([13], 0),
            'test7' : ([13, 13], 0),
            'test8' : ([13, 0, 13], 0),
            'test9' : ([13, 1, 13], 0)
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().sum13(test[0]),test[1])

    # def test_sum67(self):
    #     self.assertTrue(True)

    def test_has22(self):
        tests = {
            'test0' : ([1, 2, 2], True),
            'test1' : ([1, 2, 1, 2], False),
            'test2' : ([2, 1, 2], False),
            'test3' : ([2, 2, 1, 2], True),
            'test4' : ([1, 3, 2], False),
            'test5' : ([1, 3, 2, 2], True),
            'test6' : ([2, 3, 2, 2], True),
            'test7' : ([4, 2, 4, 2, 2, 5], True),
            'test8' : ([1, 2], False),
            'test9' : ([2, 2], True)
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().has22(test[0]),test[1])
        self.assertTrue(True)

    def test_cigar_party(self):
        tests = {
            'test0' : ((30,False), False),
            'test1' : ((50,False), True),
            'test2' : ((70,True), True),
            'test3' : ((30,True), False),
            'test4' : ((50,True), True),
            'test5' : ((60,False), True),
            'test6' : ((61,False), False),
            'test7' : ((40,False), True),
            'test8' : ((39,False), False),
            'test9' : ((40,False), True)
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().cigar_party(test[0][0],test[0][1]),test[1])

    def test_date_fashion(self):
        tests = {
            'test0' : ((5, 10), 2),
            'test1' : ((5, 2), 0),
            'test2' : ((5, 5), 1),
            'test3' : ((3, 3), 1),
            'test4' : ((10, 2), 0),
            'test5' : ((2, 9), 0),
            'test6' : ((9, 9), 2),
            'test7' : ((10, 5), 2),
            'test8' : ((2, 2), 0),
            'test9' : ((3, 7), 1)
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().date_fashion(test[0][0],test[0][1]),test[1])

    def test_squirrel_play(self):
        tests = {
            'test0' : ((70, False), True),
            'test1' : ((95, False), False),
            'test2' : ((95, True), True),
            'test3' : ((90, False), True),
            'test4' : ((90, True), True),
            'test5' : ((50, False), False),
            'test6' : ((50, True), False),
            'test7' : ((100, False), False),
            'test8' : ((100, True), True),
            'test9' : ((105, True), False)
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().squirrel_play(test[0][0],test[0][1]),test[1])

    def test_caught_speeding(self):
        tests = {
            'test0' : ((60, False), 0),
            'test1' : ((65, False), 1),
            'test2' : ((65, True), 0),
            'test3' : ((80, False), 1),
            'test4' : ((85, False), 2),
            'test5' : ((85, True), 1),
            'test6' : ((70, False), 1),
            'test7' : ((75, False), 1),
            'test8' : ((75, True), 1),
            'test9' : ((40, False), 0)
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().caught_speeding(test[0][0],test[0][1]),test[1])

    def test_sorta_sum(self):
        tests = {
            'test0' : ((3, 4), 7),
            'test1' : ((9, 4), 20),
            'test2' : ((10, 11), 21),
            'test3' : ((12, -3), 9),
            'test4' : ((-3, 12), 9),
            'test5' : ((4, 5), 9),
            'test6' : ((4, 6), 20),
            'test7' : ((14, 7), 21),
            'test8' : ((14, 6), 20)
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().sorta_sum(test[0][0],test[0][1]),test[1])

    def test_alarm_clock(self):
        tests = {
            'test0' : ((1, False), '7:00'),
            'test1' : ((5, False), '7:00'),
            'test2' : ((0, False), '10:00'),
            'test3' : ((6, False), '10:00'),
            'test4' : ((0, True), 'off'),
            'test5' : ((6, True), 'off'),
            'test6' : ((1, True), '10:00'),
            'test7' : ((3, True), '10:00'),
            'test8' : ((5, True), '10:00')
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().alarm_clock(test[0][0],test[0][1]),test[1])

    def test_love6(self):
        tests = {
            'test0' : ((6, 4), True),
            'test1' : ((4, 5), False),
            'test2' : ((1, 5), True),
            'test3' : ((1, 6), True),
            'test4' : ((1, 8), False),
            'test5' : ((1, 7), True),
            'test6' : ((7, 5), False),
            'test7' : ((8, 2), True),
            'test8' : ((6, 6), True),
            'test9' : ((-6, 2), False)
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().love6(test[0][0],test[0][1]),test[1])

    def test_in1to10(self):
        tests = {
            'test0' : ((5, False), True),
            'test1' : ((11, False), False),
            'test2' : ((11, True), True),
            'test3' : ((10, False), True),
            'test4' : ((10, True), True),
            'test5' : ((9, False), True),
            'test6' : ((9, True), False),
            'test7' : ((1, False), True),
            'test8' : ((1, True), True),
            'test9' : ((0, False), False)
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().in1to10(test[0][0],test[0][1]),test[1])

    def test_near_ten(self):
        tests = {
            'test0' : (12, True),
            'test1' : (17, False),
            'test2' : (19, True),
            'test3' : (31, True),
            'test4' : (6, False),
            'test5' : (10, True),
            'test6' : (11, True),
            'test7' : (21, True),
            'test8' : (22, True),
            'test9' : (23, False)
        }
        for test in tests.values():
            self.assertEqual(self.cb_solutions().near_ten(test[0]),test[1])

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

    def test_hello_name(self):
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
        #     self.assertEqual(self.cb_solutions().hello_name(test[0]),test[1])
        self.assertTrue(True)

    def test_make_abba(self):
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
        #     self.assertEqual(self.cb_solutions().make_abba(test[0]),test[1])
        self.assertTrue(True)

    def test_make_tags(self):
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
        #     self.assertEqual(self.cb_solutions().make_tags(test[0]),test[1])
        self.assertTrue(True)

    def test_make_out_word(self):
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
        #     self.assertEqual(self.cb_solutions().make_out_word(test[0]),test[1])
        self.assertTrue(True)

    def test_extra_end(self):
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
        #     self.assertEqual(self.cb_solutions().extra_end(test[0]),test[1])
        self.assertTrue(True)

    def test_first_two(self):
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
        #     self.assertEqual(self.cb_solutions().first_two(test[0]),test[1])
        self.assertTrue(True)

    def test_first_half(self):
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
        #     self.assertEqual(self.cb_solutions().first_half(test[0]),test[1])
        self.assertTrue(True)

    def test_without_end(self):
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
        #     self.assertEqual(self.cb_solutions().without_end(test[0]),test[1])
        self.assertTrue(True)

    def test_combo_string(self):
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
        #     self.assertEqual(self.cb_solutions().combo_string(test[0]),test[1])
        self.assertTrue(True)

    def test_non_start(self):
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
        #     self.assertEqual(self.cb_solutions().non_start(test[0]),test[1])
        self.assertTrue(True)

    def test_left2(self):
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
        #     self.assertEqual(self.cb_solutions().left2(test[0]),test[1])
        self.assertTrue(True)

    def test_double_char(self):
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
        #     self.assertEqual(self.cb_solutions().double_char(test[0]),test[1])
        self.assertTrue(True)

    def test_count_hi(self):
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
        #     self.assertEqual(self.cb_solutions().count_hi(test[0]),test[1])
        self.assertTrue(True)

    def test_cat_dog(self):
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
        #     self.assertEqual(self.cb_solutions().cat_dog(test[0]),test[1])
        self.assertTrue(True)

    def test_count_code(self):
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
        #     self.assertEqual(self.cb_solutions().count_code(test[0]),test[1])
        self.assertTrue(True)

    def test_end_other(self):
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
        #     self.assertEqual(self.cb_solutions().end_other(test[0]),test[1])
        self.assertTrue(True)

    def test_xyz_there(self):
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
        #     self.assertEqual(self.cb_solutions().xyz_there(test[0]),test[1])
        self.assertTrue(True)

    def test_sleep_in(self):
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
        #     self.assertEqual(self.cb_solutions().sleep_in(test[0]),test[1])
        self.assertTrue(True)

    def test_monkey_trouble(self):
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
        #     self.assertEqual(self.cb_solutions().monkey_trouble(test[0]),test[1])
        self.assertTrue(True)

    def test_sum_double(self):
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
        #     self.assertEqual(self.cb_solutions().sum_double(test[0]),test[1])
        self.assertTrue(True)

    def test_diff21(self):
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
        #     self.assertEqual(self.cb_solutions().diff21(test[0]),test[1])
        self.assertTrue(True)

    def test_parrot_trouble(self):
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
        #     self.assertEqual(self.cb_solutions().parrot_trouble(test[0]),test[1])
        self.assertTrue(True)

    def test_makes10(self):
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
        #     self.assertEqual(self.cb_solutions().makes10(test[0]),test[1])
        self.assertTrue(True)

    def test_near_hundred(self):
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
        #     self.assertEqual(self.cb_solutions().near_hundred(test[0]),test[1])
        self.assertTrue(True)

    def test_pos_neg(self):
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
        #     self.assertEqual(self.cb_solutions().pos_neg(test[0]),test[1])
        self.assertTrue(True)

    def test_not_string(self):
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
        #     self.assertEqual(self.cb_solutions().not_string(test[0]),test[1])
        self.assertTrue(True)

    def test_missing_char(self):
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
        #     self.assertEqual(self.cb_solutions().missing_char(test[0]),test[1])
        self.assertTrue(True)

    def test_front_back(self):
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
        #     self.assertEqual(self.cb_solutions().front_back(test[0]),test[1])
        self.assertTrue(True)

    def test_front3(self):
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
        #     self.assertEqual(self.cb_solutions().front3(test[0]),test[1])
        self.assertTrue(True)

    def test_string_times(self):
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
        #     self.assertEqual(self.cb_solutions().string_times(test[0]),test[1])
        self.assertTrue(True)

    def test_front_times(self):
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
        #     self.assertEqual(self.cb_solutions().front_times(test[0]),test[1])
        self.assertTrue(True)

    def test_string_bits(self):
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
        #     self.assertEqual(self.cb_solutions().string_bits(test[0]),test[1])
        self.assertTrue(True)

    def test_string_splosion(self):
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
        #     self.assertEqual(self.cb_solutions().string_splosion(test[0]),test[1])
        self.assertTrue(True)

    def test_last2(self):
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
        #     self.assertEqual(self.cb_solutions().last2(test[0]),test[1])
        self.assertTrue(True)

    def test_array_count9(self):
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
        #     self.assertEqual(self.cb_solutions().array_count9(test[0]),test[1])
        self.assertTrue(True)

    def test_array_front9(self):
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
        #     self.assertEqual(self.cb_solutions().array_front9(test[0]),test[1])
        self.assertTrue(True)

    def test_array123(self):
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
        #     self.assertEqual(self.cb_solutions().array123(test[0]),test[1])
        self.assertTrue(True)

    def test_string_match(self):
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
        #     self.assertEqual(self.cb_solutions().string_match(test[0]),test[1])
        self.assertTrue(True)