import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'C:/Users/nicol/Documents/ProyectoPython/Selenium-Python/chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        driver = self.driver
        driver.get('https://github.com/NicolasImplant')

    def test_visit_linkedin(self):
        self.driver.get('https://www.linkedin.com/in/nicolasimplant/')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='Hello World Report'))