import unittest
from selenium import webdriver
from google_page import GooglePage

class GoogleTest(unittest.TestCase):

    @classmethod    
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path= r'C:/Users/nicol/Documents/ProyectoPython/Selenium-Python/chromedriver.exe')

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('blink 182')

        self.assertEqual('blink 182', google.keyword)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity = 2)
    