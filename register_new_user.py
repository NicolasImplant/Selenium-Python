import unittest
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:/Users/nicol/Documents/ProyectoPython/Selenium-Python/chromedriver.exe')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(30)


# Ubicamos el boton account, generamos un click y, mediante el nombre de la opccion ingresamos en Log In 

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()

# Verificamos en primer lugar el boton de crear cuenta, validamos que el boton este disponible y habilitado
# al realizar las validaciones de manera correcta generamos un click para iniciar la creacion del usuario

        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

# Validamos a través del titulo de la pestaña que nos encontremos en la pagina correcta para realizar la creacion del usuario

        self.assertEqual('Create New Customer Account', driver.title)

# Escribimos en cada uno de los campos de texto los datos creando variables para cada valor requerido

        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')        
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        news_letter_subscription = driver.find_element_by_id('is_subscribed')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')

# Validamos que cada uno de los botones se encuentre habilitado

        self.assertTrue(
            first_name.is_enabled() and
            middle_name.is_enabled() and
            last_name.is_enabled() and
            email_address.is_enabled() and
            password.is_enabled() and
            confirm_password.is_enabled() and
            news_letter_subscription.is_enabled() and
            submit_button.is_enabled())

# Una vez validamos que esten habilitados enviamos los valores a cada variable con el metodo .send_keys(), a su vez se genera
# una espera de 2 segundos entre el ingreso de cada dato

        first_name.send_keys('Test')
        driver.implicitly_wait(2)
        middle_name.send_keys('Test')
        driver.implicitly_wait(2)
        last_name.send_keys('Test')
        driver.implicitly_wait(2)
        email_address.send_keys('Test@testingInfo.com')
        driver.implicitly_wait(2)
        password.send_keys('Test')
        driver.implicitly_wait(2)
        confirm_password.send_keys('Test')
        driver.implicitly_wait(2)
        submit_button.click()


    def tearDown(self):
        self.driver.implicitly_wait(15)
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity = 2)    