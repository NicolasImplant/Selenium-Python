import unittest
from selenium import webdriver
from time import sleep

class MercadoLibreTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:/Users/nicol/Documents/ProyectoPython/Selenium-Python/chromedriver.exe')
        driver = self.driver
        driver.get('https://www.mercadolibre.com')
        driver.maximize_window()
        driver.implicitly_wait(30)

    def test_mercadolibre_search_ps4(self):
        driver = self.driver
        country = driver.find_element_by_id('CO').click()

        search_field = driver.find_element_by_class_name('nav-search-input')
        search_field.click()
        search_field.send_keys('playstation 4')
        search_field.submit()
        sleep(3)

        location = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/aside/section/div[9]/ul/li[1]/a')
        location.click()
        sleep(3)

        condition = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/aside/section/div[7]/ul/li[1]/a')
        condition.click()
        sleep(3)

        order_menu = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/section/div[1]/div/div/div/div[2]/div/div')
        order_menu.click()
        sleep(3)

        select_price = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/section/div[1]/div/div/div/div[2]/div/div/div/ul/a[2]/div[2]/div[2]/div')
        select_price.click()
        sleep(3)

        articles = []
        prices   = []

        for i in range(5):
            article_name = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[1]/a/h2')
            article_name.text
            articles.append(article_name)
            article_price = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[2]/div[1]/div[1]/a/div/div/span[1]/span[2]/span[2]')
            article_price.text
            prices.append(article_price)

        print(articles,prices)
        
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity = 2)