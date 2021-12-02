import unittest
from selenium import webdriver

class TyposTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'C:/Users/nicol/Documents/ProyectoPython/Selenium-Python/chromedriver.exe')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Typos').click()

    def test_typos(self):
        driver = self.driver

        # Se crea una variable para verificar el contenido del texto
        paragraph_to_check = driver.find_element_by_xpath('//*[@id="content"]/div/p[2]')
        text_to_check = paragraph_to_check.text

        # Variables de control
        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."

        # Ciclo que garantiza que tomamos el texto correcto

        while text_to_check != correct_text:
            paragraph_to_check = driver.find_element_by_xpath('//*[@id="content"]/div/p[2]')
            text_to_check = paragraph_to_check.text
            driver.refresh()
            tries += 1


        while not found:
            if text_to_check == correct_text:
                found = True   

        self.assertEqual(found, True)

        print(f'It took {tries} tries to find the typo')



    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity = 2)