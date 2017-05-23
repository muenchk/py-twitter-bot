# https://docs.python.org/2/library/unittest.html
import unittest

from tweet_text import idle_text

# The basic building blocks of unit testing are test cases
# single scenarios that must be set up and checked for correctness.
# In unittest, test cases are represented by instances of unittest's TestCase class.
# To make your own test cases you must write subclasses of TestCase.

class TestTweetText(unittest.TestCase):
    # This is called immediately before calling each test method
    def setUp(self):
        self.text1 = idle_text()
        self.text2 = idle_text()

    def test_start(self):
        # In order to test something, we use one of the assert*()
        # methods provided by the TestCase base class
        # https://docs.python.org/2/library/unittest.html#unittest.TestCase.assertTrue
        Count = 0
        for d in range (0, 100000):
            self.text1 = idle_text()
            self.text2 = idle_text()
            if (not(self.text1 == self.text2)):
                Count = Count + 1
            

        self.assertEqual(Count, 100000)
        #self.assertNotEqual(self.text1, self.text2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
