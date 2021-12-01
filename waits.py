import unittest
from selenium import webdriver
# By es un metodo que nos permite seleccionar un elemento de un sitio web a través de su selector
from selenium.webdriver.common.by import By
# Nos permite usar las expected conditions y manejar las esperas explicitas
from selenium.webdriver.support.ui import WebDriverWait
# Importamos las expected conditions
from selenium.webdriver.support import expected_conditions as EC

class ExplicitWaitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:/Users/nicol/Documents/ProyectoPython/Selenium-Python/chromedriver.exe')
        self.driver.get('http://demo-store.seleniumacademy.com/')

    def test_account_link(self):

        # WebDriver va a hacer referencia de self.driver, maximo por 10 segundos hasta, que se cumpla la condicion esperada
        # dicha condicion está dada por la funcion lamda que recibe como parametro un .... y a traves del id
        # compara el atributo de tamaño de lista con un valor predeterminado de 3 o número de idiomas posibles        
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id('select-language').get_attribute('length') == '3')
        
        # Referencia al enlace donde estan las cuentas a través de web driver, por un maximo de 10 segundos, hasta que se cumpla
        # la condicion esperada, en este caso que un elemento con el nombre 'ACCOUNT' sea visible. 
        account = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'ACCOUNT')))

        # Damos click en 'ACCOUNT'
        account.click()   

    def test_create_new_costumer(self):
        # Le pedimos a driver que encuentre y de click en el elemento que en su link tiene el texto 'ACCOUT'
        self.driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click()    

        # Le pedimos a webdriverwait que sea self.driver, durante un maximo de 10 segundos, hasta que se cumpla la condición
        # esperada, en este caso que el elemento my account sea visible en el sitio web, NOTA: el parametro debe estar escrito
        # de la misma manera que en el sitio web 
        my_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.LINK_TEXT, 'My Account')))
        #Ingresamos a my account
        my_account.click()

        
        # Le pedimos a webdriverwait que sea self.driver, durante un maximo de 10 segundos, hasta que se cumpla la condición
        # esperada, en este caso que el elemento cuyo nombre sea 'CREATE AN ACCOUNT' sea clickeable 

        create_account_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        
        # Ingresamos
        create_account_button.click()

        # Verificamos que la página web sea la correcta validando el nombre de la misma.
        WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Coustomer Account'))

    def tearDown(self):
        self.driver.close()
    

if __name__ == '__main__':
    unittest.main(verbosity = 2)
    