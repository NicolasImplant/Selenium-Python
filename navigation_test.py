import unittest
from selenium import webdriver
# Es una manera de generar pausas que permitan vizualizar el flujo del navegador, sin embargo no es recomendable
# ya que agrega varios segundos de tiempo a la ejecución
from time import sleep

class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:/Users/nicol/Documents/ProyectoPython/Selenium-Python/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://www.google.com/')

    def test_browsing_navigation(self):
        driver = self.driver
        # Para manipular la barra de busqueda de google creamos una nueva variable, a partir de esta variable
        # generamos una busqueda en el navegador
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('nicolasimplant')
        search_field.submit()
        
        # Metodos para retroceder, avanzar y refrescar el navegador
        driver.back()
        sleep(3)
        driver.forward()
        sleep(3)
        driver.refresh()
        sleep(3)
        # Se han añadido 9 segundos a la ejecución    

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity = 2)