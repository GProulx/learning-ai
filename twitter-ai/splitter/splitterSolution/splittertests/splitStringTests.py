import unittest
import splitter

class Test_SplitString(unittest.TestCase):

    def test_normal_string(self):
        inputString = "The quick brown fox jumps over the lazy dog"
        result = splitter.splitter.splitString(inputString)
        expected = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
        self.assertEqual(result, expected)

    def test_remove_coma(self):
        inputString = "#MachineLearning, #DataViz, and #AI"
        result = splitter.splitter.splitString(inputString)
        expected = ["#MachineLearning", "#DataViz", "and", "#AI"]
        self.assertEqual(result, expected)

    def test_remove_dot(self):
        inputString = "The quick brown fox jumps over the lazy dog. Period."
        result = splitter.splitter.splitString(inputString)
        expected = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog", "Period"]
        self.assertEqual(result, expected)

    def test_remove_dot_for_numbers_without_decimal_part(self):
        # Regex to use to try to fix that error : ^[1-9]\d*(\.\d+)?$  
        inputString = "This appends in 2018. After something."
        result = splitter.splitter.splitString(inputString)
        expected = ["This", "appends", "in", "2018", "After", "something"]
        self.assertEqual(result, expected)

# Other problem, shouldn't split : cenotediving@mail.com

if __name__ == '__main__':
    unittest.main()
