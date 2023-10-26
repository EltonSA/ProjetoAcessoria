from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import app
import time
import openpyxl
import threading


def set_temp_text(event, entry, temp_text):
    if entry.get() == temp_text:
        entry.delete(0, "end")  # Limpa o texto temporário

def clear_temp_text(event, entry, temp_text):
    if not entry.get():
        entry.insert(0, temp_text)  # Se o Entry estiver vazio, insira o texto temporário

# Função chamada pelo botão ENTRAR, que chama outra função no arquivo App.py
userDados = []
caminhoPlanilha = ''

def salvarLogin():
    userLogin = login.get()
    userPassword = senha.get()
    userPlanilha = planilha.get()
    userDados.append(userLogin)
    userDados.append(userPassword)
    userDados.append(userPlanilha)
    userMarcarDepartamento()

def userMarcarDepartamento():
    app.teste(userDados[0], userDados[1], userDados[2])

def selecionarArquivo():
    file_path = filedialog.askopenfilename(title="Selecionar uma planilha", filetypes=[("Planilhas Excel", "*.xlsx")])

    planilha.delete(0, "end")  # Limpa o campo de planilha
    planilha.insert(0, file_path)  # Insere o caminho do arquivo selecionado


janela = Tk()
janela.title("MailWave")
janela.geometry("720x600+610+153")
#janela.iconbitmap(default="C:\\Users\\elton.santos\\Desktop\\projetos\\emailEXE\\icones\\logo.ico")

#img_fundo = PhotoImage(file="C:\\Users\\elton.santos\\Desktop\\projetos\\emailEXE\\imagens\\layout.png")
#lab_fundo = Label(janela, image=img_fundo)
#lab_fundo.pack()

login_temp_text = ""
senha_temp_text = ""
planilha_temp_text = ""

login = Entry(janela,
              fg="white",
              background="#1E2124",
              bd=2,
              font=("Arimo", 11),
              justify=CENTER,
              )
login.insert(0, login_temp_text)
login.place(x=60, y=213, width=282, height=45)

senha = Entry(janela,
              fg="white",
              background="#1E2124",
              bd=2,
              font=("Arimo", 11),
              justify=CENTER,
              show="*",
              )
senha.insert(0, senha_temp_text)
senha.place(x=60, y=293, width=282, height=45)

planilha = Entry(janela,
                fg="#505050",
                background="#1E2124",
                bd=2,
                font=("Arimo", 11),
                justify=CENTER,
                )
planilha.insert(0, planilha_temp_text)
planilha.place(x=60, y=373, width=282, height=45)

butao = Button(janela,
               bd=2,
               fg="white",
               font=("Arimo", 11),
               justify=CENTER,
               text="Entrar",
               background="#8F01EC",
               command=salvarLogin,
   
               )
butao.place(x=161, y=529, width=80, height=39)

selecionar_planilha = Button(janela, text="Selecionar Planilha", fg="white", command=selecionarArquivo, background="#8F01EC")
selecionar_planilha.place(x=125, y=430, width=148, height=40)

janela.mainloop()
