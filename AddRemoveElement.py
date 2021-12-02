import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'C:/Users/nicol/Documents/ProyectoPython/Selenium-Python/chromedriver.exe')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.maximize_window()
        driver.find_element_by_link_text('Add/Remove Elements').click()
    
# Añadir y remover elementos de un sitio web

    def test_add_remove(self):
        driver = self.driver

        # Cuantos son los elementos que se van a agregar
        elements_added = int(input('How many elements will you add?:  '))
        # Cuantos elementos vamos a remover
        elements_removed = int(input('How many elements will you remove?:   '))
        # Diferencia entre los elementos
        Total_elements = elements_added - elements_removed
        # Boton para añadir elementos
        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')        
        sleep(3)        

        # Ciclo for que crea los botones 
        for i in range(elements_added):
            add_button.click()

        # Ciclo for que elimina los botones, en caso de intentar eliminar mas de los que existen se levanta una excepcion
        for i in range(elements_removed):
            try:
                delete_button = driver.find_element_by_xpath('//*[@id="elements"]/button')
                delete_button.click()
            except:
                print("You´re trying do delet more elements the existent")
                break

        # Mostrar en consola lo que ha ocurrido

        if Total_elements > 0:
            print(f'There are {Total_elements} elements on screen')
        else:
            print('There are 0 elements on screen')
        
        sleep(3)


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity = 2)
