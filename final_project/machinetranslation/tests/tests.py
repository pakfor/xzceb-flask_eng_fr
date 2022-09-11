import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnToFr(unittest.TestCase):
    def testNull(self):
        self.assertNotEqual(englishToFrench("None"), '')
        self.assertNotEqual(englishToFrench(0), 0)
    def testHello(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

class TestFrToEn(unittest.TestCase):
    def testNull(self):
        self.assertNotEqual(frenchToEnglish("None"), '')
        self.assertNotEqual(frenchToEnglish(0), 0)
    def testHello(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

if __name__ == "__main__":
    unittest.main()
