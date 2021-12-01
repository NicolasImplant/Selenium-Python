import unittest
from selenium import webdriver

class CompareProducts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:/Users/nicol/Documents/ProyectoPython/Selenium-Python/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

# Metodo para manejar alerts

    def test_compare_products_removal_alert(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()

# Escribimos en la barra de busqueda el termino que queremos encontrar, en este caso es "tee" y lo enviaremos

        search_field.send_keys('tee')
        search_field.submit()

# Buscamos el elemento requerido para generar el alert

        driver.find_element_by_class_name('link-compare').click()

# Una vez se ha encontrado el elemento para comparar procedemos a eliminarlo, como el elemento no tiene asignada una clase o
# id, procedemos a buscarlo por el texto

        driver.find_element_by_link_text('Clear All').click()

# Todo lo anterior disparará el alert de la página, para interactuar con el creamos la variable alert, y pedimos que realice
# un cambio de foco para que el click desvíe su atencion hacia el alert

        alert = driver.switch_to.alert

# Ahora extraemos el texto que nos muestra en una nueva varible

        alert_text = alert.text

# Verificamos que el texto del alert sea el mismo que estamos esperando

        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)

# Por útimo simulamos un click en aceptar

        alert.accept()


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity = 2)

