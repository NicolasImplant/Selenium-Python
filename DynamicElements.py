import unittest
from selenium import webdriver
from time import sleep

class DynamicElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'C:/Users/nicol/Documents/ProyectoPython/Selenium-Python/chromedriver.exe')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')  
        driver.find_element_by_link_text('Disappearing Elements').click()

    def test_name_elements(self):
        driver = self.driver
        # Creamos una lista vacía que corresponde a las opciones del menu en la pagina
        options = []
        # La variable menu contiene la cantidad de elementos conocida
        menu = 5
        # Esta variable será el conteo de intentos que realizará Selenium
        tries = 1

        while len(options) < 5:
            # La lista options se vacía a cada paso para iterar de manera continua
            options.clear()

            for i in range(menu):
                try:
                    # Dado que el ciclo inicia en el valor de cero, sumamos uno a la variable i, ya que los elementos inician desde 1
                    options_name = driver.find_element_by_xpath(f'/html/body/div[2]/div/div/ul/li[{i+1}]/a')
                    options.append(options_name.text)
                    print(options)
                except:
                    print(f'Option number {i+1} is Not found')
                    tries += 1
                    driver.refresh()
        
        print(f'Finished in {tries} tries')


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity = 2)