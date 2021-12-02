import unittest
from selenium import webdriver
# Nuevamente importamos las expected conditions para este ejercicio
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class DynamicControlsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'C:/Users/nicol/Documents/ProyectoPython/Selenium-Python/chromedriver.exe')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Dynamic Controls').click()

    def test_dynamic_controls(self):
        driver = self.driver

        # Identificamos el elemento checkbox inicialmente

        checkbox = driver.find_element_by_css_selector('#checkbox > input[type=checkbox]')
        checkbox.click()

        # Identificamos el boton para eliminar el checkbox

        remove_add_button = driver.find_element_by_css_selector('#checkbox-example > button')
        remove_add_button.click()

        # Esperamos mientras ejecuta el comando add o remove

        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button')))
        remove_add_button.click()

        # Boton para habilitar/deshabilitar la caja de texto de la pagina

        enable_disable_button = driver.find_element_by_css_selector('#input-example > button')
        enable_disable_button.click()

        # Esperamos mientras se habilita la caja de texto

        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#input-example > button')))

        # Variable que corresponde a la caja de texto

        text_area = driver.find_element_by_css_selector('#input-example > input[type=text]')
        text_area.send_keys('Hola Mundo!')

        # Finalmente damos click para deshabilitar la caja de texto
        
        enable_disable_button.click()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity = 2)