import unittest
import splitter

class Test_RemoveBasicWords(unittest.TestCase):

    def test_basic_words(self):
        inputString = "The quick brown fox jumps over the lazy dog"
        result = splitter.splitter.removeBasicWords(inputString.split())
        expected = ["quick", "brown", "fox", "jumps", "over", "lazy", "dog"]
        self.assertEqual(result, expected)

    def test_basic_words_french(self):
        inputString = "La table de la maison du village."
        result = splitter.splitter.removeBasicWords(inputString.split())
        expected = ["table", "maison", "village."]
        self.assertEqual(result, expected)

    def test_basic_words_french_table(self):
        inputString = "La des les ma nos ces ses mes leurs"
        result = splitter.splitter.removeBasicWords(inputString.split())
        expected = []
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
