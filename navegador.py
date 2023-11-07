from selenium import webdriver
from selenium.webdriver.support.select import Select 
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class navegadorAcessorias:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        #self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        #self.options.add_argument('window-size=945x1012')
        self.driver = webdriver.Chrome(options=self.options)

    def abrirBrowser(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get("https://app.acessorias.com")

        