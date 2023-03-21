from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from recursos_externos import senha, contas, mensagem, usuario# INFORMAÇÕES MANTIDAS EM OUTRO PROGRAMA PARA MANTER O SIGILO

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.maximize_window()

navegador.get("https://www.instagram.com/")
time.sleep(2)


# FAZ O LOGIN
navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(usuario)
time.sleep(2)

navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(senha)
time.sleep(2)

navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[3]').click()
time.sleep(5)


# CLICA NO BOTÃO "AGORA NÃO" DO SALVAR INFORMAÇÕES
navegador.find_element('xpath', '//div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button').click()
time.sleep(2)

# CLICA NO BOTÃO "AGORA NÃO" DE HABILITAR NOTIFICAÇÕES
navegador.find_element('xpath', '//div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
time.sleep(2)

# FUNÇÃO PARA BUSCAR AS CONTAS NA LISTA
def buscar_conta(conta):

    # CLICA NO BOTÃO DE PESQUISA 
    botao_pesquisa = navegador.find_element('xpath', '//div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div/div[2]/div/div')
    botao_pesquisa.click()
    time.sleep(2)
    
    # PESQUISA AS CONTAS PRESENTES NA LISTA
    campo_pesquisa = navegador.find_element('xpath', '//div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
    campo_pesquisa.send_keys(conta)
    time.sleep(2)
    campo_pesquisa.send_keys(Keys.ENTER)
    time.sleep(5)

    # SEGUE A CONTA
    botao_seguir = navegador.find_element('xpath', '//div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
    botao_seguir.click()
    time.sleep(2)

    # CLICA NO BOTÃO "ENVIAR MENSAGEM" NO PERFIL
    botao_enviar_msg = navegador.find_element('xpath', '//div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div')
    time.sleep(3)
    botao_enviar_msg.click()
    time.sleep(10)


# FUNÇÃO PARA ENVIAR A MENSAGEM 
def enviar_mensagem(mensagem):

    # CLICA NO CAMPO DE TEXTO DO DIRECT E ENVIA A MSG
    campo_texto = navegador.find_element('xpath','//div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
    campo_texto.send_keys(mensagem)
    time.sleep(10)
    campo_texto.send_keys(Keys.ENTER)
    time.sleep(180)

    # VOLTA PRA PAGINA INICIAL PARA EXECUTAR A FUNÇÃO buscar_conta() NOVAMENTE
    pagina_inicial = navegador. find_element('xpath', '//div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div')
    pagina_inicial.click()
    time.sleep(2)


# LOOP PARA BUSCAR AS RESPECTIVAS CONTAS E MENSAGEM
for conta in contas:
    buscar_conta(conta)
    enviar_mensagem(mensagem)




