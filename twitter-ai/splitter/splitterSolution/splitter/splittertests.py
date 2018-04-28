import unittest
import splitter

class Test_test1(unittest.TestCase):
   
    def test_basic(self):
        result = splitter.splitter.extract("First Word")
        expected = ["First", "Word", "First Word"]
        self.assertEqual(result, expected)

    def test_emptyStringShouldWork(self):
        result = splitter.splitter.extract("")
        expected = []
        self.assertEqual(result, expected)

    def test_hashTagShouldBeKeep(self):
        result = splitter.splitter.extract("#AI")
        expected = ["#AI"]
        self.assertEqual(result, expected)

    def test_trailingSpaceShouldBeRemoved(self):
        result = splitter.splitter.extract(" First Word   ")
        expected = ["First", "Word", "First Word"]
        self.assertEqual(result, expected)

    def test_longerString(self):
        result = splitter.splitter.extract("The quick brown fox jumps over the lazy dog")
        expected = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog", "The quick", "quick brown", "brown fox", "fox jumps", "jumps over", "over the", "the lazy", "lazy dog"]
        self.assertEqual(result, expected)

    def test_removeDuplicates(self):
        result = splitter.splitter.extract("PADI PADI PADI USA #PADI")
        expected = ["PADI", "USA", "#PADI", "PADI PADI", "PADI USA", "USA #PADI"]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
