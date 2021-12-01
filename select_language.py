import unittest
from selenium import webdriver
from selenium.webdriver.support import select
# Se debe importar un nuevo módulo para manipular los dropDown y las listas
from selenium.webdriver.support.ui import Select 

class LanguageOptions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'C:/Users/nicol/Documents/ProyectoPython/Selenium-Python/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_select_language(self):

# Se crea una lista que incluya los idiomas disponibles en la pagina, los elementos de la lista deben estar en el mismo orden
# que se encuentran en la pagina

        exp_options = ['English', 'French', 'German'] 

# Se crea una lista vacía para almacenar las opciones que escojamos

        act_options = []

# Para manipular los elementos del dropDown crearemos una variable y llamamos el metodo "Select"

        select_language = Select(self.driver.find_element_by_id('select-language'))

# Validamos que existan las tres opciones que esperamos

        self.assertEqual(3, len(select_language.options))

# Iteramos por cada una de las opciones y alamacenar en la lista el nombre de cada opcion

        for option in select_language.options:
            act_options.append(option.text)

# Validamos que ambas listas son identicas.

        self.assertListEqual(exp_options, act_options)

# Seleccionamos un idioma validando que el ingles sea el primer idioma por defecto

        self.assertEqual('English', select_language.first_selected_option.text)
        select_language.select_by_visible_text('German')

# Validamos que el sitio esté en el idioma que eligimos

        self.assertTrue('store=german' in self.driver.current_url)

# Regresamos la página a su lenguaje por defecto utilizando los indices del dropDown

        select_language = Select(self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)


    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity = 2)