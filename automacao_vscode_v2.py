# IMPORTS
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from openpyxl import Workbook, load_workbook
from recursos_externos import senha, mensagem, usuario, aba_ativa # INFORMAÇÕES MANTIDAS EM OUTRO PROGRAMA PARA MANTER O SIGILO

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.maximize_window()

navegador.get("https://www.instagram.com/")
time.sleep(2)

# REALIZA O LOGIN DA CONTA
def faz_login(usuario, senha):
    campo_pesquisa = navegador.find_element('xpath', '//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
    campo_pesquisa.send_keys(usuario)
    time.sleep(2)

    campo_senha = navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input')
    campo_senha.send_keys(senha)
    time.sleep(2)

    botao_entrar = navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[3]/button')
    botao_entrar.click()
    time.sleep(5)


# CLICA NO BOTÃO "AGORA NÃO" DO SALVAR INFORMAÇÕES
def diz_nao():
    bota_diz_nao = navegador.find_element('xpath', '//div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
    bota_diz_nao.click()
    time.sleep(2)

    # CLICA NO BOTÃO "AGORA NÃO" DE HABILITAR NOTIFICAÇÕES
    botao_diz_nao_2 = navegador.find_element('xpath', '//div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
    botao_diz_nao_2.click()
    time.sleep(2)

# FUNÇÃO PARA BUSCAR AS CONTAS NA LISTA
def buscar_conta(conta):

    # CLICA NO BOTÃO DE PESQUISA 
    botao_pesquisa = navegador.find_element('xpath', '//div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div/div[2]/div/div')
    botao_pesquisa.click()
    time.sleep(2)
    
    # PESQUISA AS CONTAS PRESENTES NA LISTA
    campo_pesquisa = navegador.find_element('xpath', '//div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
    campo_pesquisa.send_keys(conta.value)
    time.sleep(2)
    campo_pesquisa.send_keys(Keys.ENTER)
    time.sleep(5)

    # SEGUE A CONTA
    botao_seguir = navegador.find_element('xpath', '//div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div/button/div/div')
    botao_seguir.click()
    time.sleep(2)

    # CLICA NO BOTÃO "ENVIAR MENSAGEM" NO PERFIL
    botao_enviar_msg = navegador.find_element('xpath', '//div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div')
    time.sleep(5)
    botao_enviar_msg.click()
    time.sleep(10)


# FUNÇÃO PARA ENVIAR A MENSAGEM 
def enviar_mensagem(mensagem):

    # CLICA NO CAMPO DE TEXTO DO DIRECT E ENVIA A MSG
    campo_texto = navegador.find_element('xpath','//div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
    campo_texto.send_keys(mensagem)
    time.sleep(10)
    campo_texto.send_keys(Keys.ENTER)
    time.sleep(180)

    # VOLTA PRA PAGINA INICIAL PARA EXECUTAR A FUNÇÃO buscar_conta() NOVAMENTE
    pagina_inicial = navegador. find_element('xpath', '//div/div/div[1]/div/div/div/div[1]/div[1]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/a/div/div[2]/div/div')
    pagina_inicial.click()
    time.sleep(2)


faz_login(usuario, senha)
diz_nao()

# LOOP PARA BUSCAR AS RESPECTIVAS CONTAS E MENSAGEM
for conta in aba_ativa["A"]:
    buscar_conta(conta)
    enviar_mensagem(mensagem)