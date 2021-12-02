
# Importamos la libreria csv para manipular este tipo de archivos
import  csv, unittest
from ddt import ddt, data, unpack
from selenium import webdriver

# Funcion que genera una lista de datos a partir de un archivo tipo csv
def get_data(file_name):
    rows= []
    data_file = open(file_name, 'r')
    reader = csv.reader(data_file)
    next (reader, None)
    for row in reader:
        rows.append(row)     
    return rows


# Colocamos el decorador en la clase de pruebas
@ddt
class SearchDDT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'C:/Users/nicol/Documents/ProyectoPython/Selenium-Python/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    # Utilizamos el decorador @data que recibe una tupla con la palabra dress y la cantidad de elementos que esperamos como resultado
    @data(*get_data('testdata.csv'))

    # El decorador unpack nos ayuda a desempaquetar las tuplas
    @unpack

    # A nuestra funcion de pueba ingresaremos nuevos argumentos
    def test_search_ddt(self,search_value, expected_count):
        driver = self.driver
        
        # Ubicamos la barra de busqueda y borramos su contenido
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        # En este caso al metodo .send_keys() no enviamos el valor de texto
        search_field .send_keys(search_value)
        search_field.submit()

        # En la variable products vamos a indentificar los productos
        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        expected_count = int(expected_count)

        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_element_by_class_name('note-msg').text
            self.assertEqual('Your search returns no results.', message)

        print(f'Found {len(products)} products')

        # Podemos verificar imprimiendo cada uno de los productos
        for product in products:
            print(product.text)

        # Validamos que tengamos todos los productos
        self.assertEqual(expected_count,len(products))

 
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)