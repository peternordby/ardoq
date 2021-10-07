import unittest
import task


class test_highest_product(unittest.TestCase):
    def test_valid_positives(self):
        test = [1, 10, 2, 6, 5, 3]
        self.assertEqual(task.highest_product(test), 10*6*5)

    def test_valid_negatives(self):
        test = [7, -4, -3, 3, 2]
        self.assertEqual(task.highest_product(test), -3*-4*7)

    def test_non_valid(self):
        test = [0, 2]
        self.assertEqual(task.highest_product(test), None)

    def test_not_list(self):
        test = 'not a list'
        self.assertRaises(AttributeError, task.highest_product, test)
