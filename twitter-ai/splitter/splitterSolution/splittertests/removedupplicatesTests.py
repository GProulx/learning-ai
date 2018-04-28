import unittest
import splitter

class Test_RemoveDupplicates(unittest.TestCase):

    def test_basic_itemsOfOnlyOneWord(self):
        input = ["PADI", "PADI", "PADI", "USA", "#PADI"]
        result = splitter.splitter.removedupplicates(input)
        expected = ["PADI", "USA", "#PADI"]
        self.assertEqual(result, expected)

    def test_normalList(self):
        input = ["PADI", "PADI", "PADI", "USA", "#PADI", "PADI PADI", "PADI PADI", "PADI USA", "USA #PADI"]
        result = splitter.splitter.removedupplicates(input)
        expected = ["PADI", "USA", "#PADI", "PADI PADI", "PADI USA", "USA #PADI"]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
