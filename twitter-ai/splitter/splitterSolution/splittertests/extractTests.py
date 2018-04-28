import unittest
import splitter

class Test_Extract(unittest.TestCase):
   
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
        expected = ["quick", "brown", "fox", "jumps", "over", "lazy", "dog", "quick brown", "brown fox", "fox jumps", "jumps over", "over lazy", "lazy dog"]
        self.assertEqual(result, expected)

    def test_removeDuplicates(self):
        result = splitter.splitter.extract("PADI PADI PADI USA #PADI")
        expected = ["PADI", "USA", "#PADI", "PADI PADI", "PADI USA", "USA #PADI"]
        self.assertEqual(result, expected)

    def test_complex_01(self):
        result = splitter.splitter.extract("DynamicWebPaige @DynamicWebPaige @Azure ☁️ Developer Advocate for #MachineLearning, #DataViz, and #AI 🤖. My ♥️ belongs to #Python🐍 & #rstats.")
        expected = ["DynamicWebPaige", "@DynamicWebPaige", "@Azure", "Developer", "Advocate", "#MachineLearning", "#DataViz", "#AI", "belongs", "#Python🐍", "#rstats", "DynamicWebPaige @DynamicWebPaige", "@DynamicWebPaige @Azure", "@Azure Developer", "Developer Advocate", "Advocate #MachineLearning", "#MachineLearning #DataViz", "#DataViz #AI", "#AI belongs", "belongs #Python🐍", "#Python🐍 #rstats"]
        self.assertEqual(result, expected)

    def test_complex_02(self):
        result = splitter.splitter.extract('DeepMindAI DeepMind Founded in 2010.  Building Artificial General Intelligence. The creators of #AlphaGo and Atari DQN')
        expected = ["DeepMindAI", "DeepMind", "Founded", "2010.", "Building", "Artificial", "General", "Intelligence", "creators", "#AlphaGo", "Atari", "DQN","DeepMindAI DeepMind", "DeepMind Founded", "Founded 2010.", "2010. Building", "Building Artificial", "Artificial General", "General Intelligence", "Intelligence creators", "creators #AlphaGo", "#AlphaGo Atari", "Atari DQN"]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
