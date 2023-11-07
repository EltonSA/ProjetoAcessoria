from selenium import webdriver
from selenium.webdriver.support.select import Select 
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import navegador
import usuario


''' class Aplicativo:
    def __init__(self):
        self.browser = navegador.navegadorAcessorias()       
        self.user = usuario.usuarioAcessorias()
    
    def appLogin(self):
        browser = self.browser
        browser.login()


app = Aplicativo() '''



# Função Teste do APP Principal
# Inicia um objeto da classe navegadorAcessorias
# Utiliza o atributo driver deste objeto para iniciar um objeto do tipo usuarioAcessorias
# Utiliza o método de boot para abrir o browser
# Utiliza o método de user para acessar a página de login
# Função criada para testar a conexão entre os arquivos e se as variáveis estão sendo passadas

def iniciarAplicativoDepartamentos(userLogin, userPassword, userPlanilha):

    boot = navegador.navegadorAcessorias()
    user = usuario.usuarioAcessorias(boot.driver, userLogin, userPassword, userPlanilha)
    boot.abrirBrowser()
    user.fazerLogin()
    user.marcarDepartamento()

def iniciarAplicativoEnvioAgendado(userLogin, userPassword, userPlanilha):

    boot = navegador.navegadorAcessorias()
    user = usuario.usuarioAcessorias(boot.driver, userLogin, userPassword, userPlanilha)
    boot.abrirBrowser()
    user.fazerLogin()
    user.marcarEnvioAgendado()



    



