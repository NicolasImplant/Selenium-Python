import unittest
from selenium import webdriver
from time import sleep

class OrderTablesTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'C:/Users/nicol/Documents/ProyectoPython/Selenium-Python/chromedriver.exe')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Sortable Data Tables').click()

    def test_order_data_tables(self):
        driver = self.driver

        # Se crea una lista vacía en donde se van a almacenar los datos
        table_data = [ [] for i in range(5)]
        print(table_data)

        # Se crea el ciclo for que iterará en las listas

        for i in range(5):
            header = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{i+1}]/span')
            table_data[i].append(header.text)
            
            # Ciclo que itera en el interior de la tabla extrayendo la informacion de las filas

            for j in range(4):
                row_data = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{j+1}]/td[{j+1}]')
                table_data[i].append(row_data.text)

        print(table_data)


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity = 2)