from selenium import webdriver
from selenium.webdriver.support.select import Select 
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pandinha
import time

class usuarioAcessorias:
    def __init__(self, driver, user, password, spreadsheet):
        self.usuario = user
        self.senha = password
        self.planilha = spreadsheet
        self.driver = driver

    def fazerLogin(self):
        driver = self.driver
        campo_user = driver.find_element(By.XPATH, "//input[@name='mailAC']")
        campo_user.clear()
        campo_user.send_keys(self.usuario)
        time.sleep(2)

        campo_senha = driver.find_element(By.XPATH, "//input[@name='passAC']")
        campo_senha.clear()
        campo_senha.send_keys(self.senha)
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(9000)

        
    def lerPlanilha(self): # Em construção
        planilhaDados = pandinha.read_csv(planilha, names=['CNPJ'])



    def excluirProcessos(self): # Em construção
        driver = self.driver
        econtinuo = driver.find_element(By.XPATH, "//*[@id='M1']/a/b")
        ActionChains(driver)\
        .move_to_element(econtinuo)\
        .perform()
        time.sleep(2)

        econtinuoUm = driver.find_element(By.XPATH, "//*[@id='M130']/a")
        ActionChains(driver)\
        .move_to_element(econtinuoUm)\
        .perform()
        time.sleep(2)

        econtinuoDois = driver.find_element(By.XPATH, "//*[@id='M128']")
        ActionChains(driver)\
        .move_to_element(econtinuoDois)\
        .perform()
        econtinuoDois.click()
        time.sleep(3)

        editar = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div/div[3]/div[1]/span/a[2]")
        editar.click()
        time.sleep(2)

        agendado = "Sim - Agendado"
        emailimediato = driver.find_element(By.XPATH,"//*[@id='EclSendMail']")
        emailimediato.send_keys(agendado)
        emailimediato.send_keys(Keys.RETURN)
        time.sleep(3)

        botaoSalvar = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div/form/div[4]/div[3]/div/button[1]')
        botaoSalvar.click()




