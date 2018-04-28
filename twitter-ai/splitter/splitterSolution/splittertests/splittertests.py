import unittest
import splitter

class Test_test1(unittest.TestCase):
    def test_A(self):
        self.fail("Not implemented")

    def basic_test(self):
        result = splitter.splitter.extract("First Word")
        expected = ["First", "Word"]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
