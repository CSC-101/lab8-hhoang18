import unittest
import group

class TestCases(unittest.TestCase):
    def test_groups_of_3_1(self):
        input = [1,2,3,4,5,6,7,8,9]
        result = [[1,2,3],[4,5,6],[7,8,9]]
        expected = group.groups_of_3(input)
        self.assertEqual(expected, result)
    def test_groups_of_3_2(self):
        input = [9,8,7,6,5,4,3,2,1]
        result = [[9,8,7],[6,5,4],[3,2,1]]
        expected = group.groups_of_3(input)
        self.assertEqual(expected,result)