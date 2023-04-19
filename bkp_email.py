# Generated by Selenium IDE
from lib2to3.pgen2 import driver
from webbrowser import Chrome
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# biblioteca para clique em coordenadas
from selenium.webdriver.common.action_chains import ActionChains
#from selenium import webdriver
import secrets



PATH = 'C:\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

email = secrets.email
senha = secrets.senha

texto_envio_encaminhamento = 'Backup recebidos'

# Test name: Untitled
# Step # | name | target | value
# 1 | open | /owa/ | 
driver.get("https://outlook.live.com/owa/")
# 2 | setWindowSize | 1200x800 | 
driver.set_window_size(1900, 800)
# 3 | click | linkText=Entrar | 
driver.find_element(By.LINK_TEXT, "Entrar").click()
# 4 | click | id=i0116 | 
driver.find_element(By.ID, "i0116").click()
# 5 | type | id=i0116 | uip.decap@policiacivil.sp.gov.br
driver.find_element(By.ID, "i0116").send_keys(email)

# 6 | click | id=idSIButton9 | 
driver.find_element(By.ID, "idSIButton9").click()


##SENHA##
time.sleep(4)
driver.find_element(By.ID, "i0118").click()
driver.find_element(By.ID, "i0118").send_keys(senha)
#clicar para enviar senha
driver.find_element(By.ID, "idSIButton9").click()

# SELECIONA TEMP - RECEBIDOS

time.sleep(6)
# 7 | mouseOver | css=.h2KSz:nth-child(4) | 
element = driver.find_element(By.CSS_SELECTOR, ".h2KSz:nth-child(4)")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
# 8 | click | css=div:nth-child(6) .BptzE > .Idtcl | 
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "div:nth-child(6) .BptzE > .Idtcl").click() #ESTE FUNCIONA
# 9 | click | xpath=//div[@id='AQAAAo5jsrcBAAACoc/WrwAAAAA=']/div/div/div | 
## driver.find_element(By.XPATH, "//div[@id=\'AQAAAo5jsrcBAAACoc/WrwAAAAA=\']/div/div/div").click() #este não funciona
# 10 | mouseOver | css=#AQAAAo5jsrcBAAACoc\/WrwAAAAA\= .y1E5h | 
## element = driver.find_element(By.CSS_SELECTOR, "#AQAAAo5jsrcBAAACoc\\/WrwAAAAA\\= .y1E5h") #este não funciona
## actions = ActionChains(driver) #este não funciona
## actions.move_to_element(element).perform() #este não funciona

# /SELECIONA TEMP - RECEBIDOS


#Clica no primeiro email apresentado
    #driver.find_element(By.XPATH, "//div[@id=\'AQAAAo5jsrcBAAACoc/YbQAAAAA=\']/div/div/div").click() #Quebrou
    #driver.find_element(By.XPATH, "//*[@id='AQAAAo5jsrcBAAACoc/WigAAAAA=']/div/div/div[1]/div/div[1]/div[1]").click() #Quebrou / USAR POSIÇÃO GLOBAL PARA CLICAR
time.sleep(2)
#click de área 
actionChains = ActionChains(driver)
button_xpath  = "//*[@id='MainModule']/div/div/div[1]/div/div/div/div/div[3]/div[1]/div" #XPATH do botão "caixa de entrada" -> dar offset à direita para clicar - o botão da caixa de entrada sempre estará à esquerda do primeiro email
button = driver.find_element_by_xpath(button_xpath)
actionChains.move_to_element(button).move_by_offset(200,0).click().perform()
#click de área

#clica no encaminhamento rápido
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='794b2300-16a8-6e9a-7c66-c76df4e1d82f']/span/div").click() #este aqui funcionou
time.sleep(5)
#Digita texto - âncora para buscar no backup
driver.find_element(By.XPATH, "//*[@id='editorParent_1']/div/div[1]").send_keys(texto_envio_encaminhamento) #DEFEITO no segundo envio



#ENVIAR
#clica em ENVIAR XPATH do botão "Favoritos" -> dar offset à direita para clicar - o botão da caixa de entrada sempre estará à esquerda do primeiro email
# botao Favoritos XPATH //*[@id='MainModule']/div/div/div[1]/div/div/div/div/div[1]/div[1]/span
#click de área 
"""actionChains = ActionChains(driver)
button_xpath  = "//*[@id='MainModule']/div/div/div[1]/div/div/div/div/div[1]/div[1]/span" #XPATH do botão "Favoritos" -> dar offset à direita 
button = driver.find_element_by_xpath(button_xpath)
actionChains.move_to_element(button).move_by_offset(200,0).click().perform()"""


ActionChains(driver)\
    .key_down(Keys.CONTROL)\
    .key_down(Keys.ENTER)\
    .perform()

ActionChains(driver)\
    .key_up(Keys.CONTROL)\
    .key_up(Keys.ENTER)\
    .perform()
#/click de área
# /ENVIAR


#clica em mover para (envia a tecla 'v')
time.sleep(3)
ActionChains(driver)\
    .send_keys("v")\
    .perform()

#digita "Temp - robo enviou" 
time.sleep(1)
ActionChains(driver)\
    .send_keys("Temp - robo enviou")\
    .perform()
#Aperta Enter para completar a movimentação de pasta
time.sleep(3)
ActionChains(driver)\
    .send_keys(Keys.ENTER)\
    .perform()


#fecha o navegador
time.sleep(3)
driver.close()
