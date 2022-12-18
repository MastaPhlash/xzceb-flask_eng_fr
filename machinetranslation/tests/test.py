import unittest
from translator.py import englishToFrench, frenchToEnglish


class TestTranslatorMethods(unittest.TestCase):
    
    #Test englishToFrench
    def test_e2f(self):

        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        
    #Test frenchToEnglish
    def test_f2e(self):

        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        
    def test_e2f_not_null(self):
    
        self.assertIsNotNone(englishToFrench('Hello'))
        
    def test_f2e_not_null(self):
    
        self.assertIsNotNone(frenchToEnglish('Bonjour'))
  
if __name__ == '__main__':
    unittest.main()
