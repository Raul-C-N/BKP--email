# Generated by Selenium IDE
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

class TestUntitled():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_untitled(self):
    # Test name: Untitled
    # Step # | name | target | value
    # 1 | open | /owa/ | 
    self.driver.get("https://outlook.live.com/owa/")
    # 2 | setWindowSize | 1200x800 | 
    self.driver.set_window_size(1200, 800)
    # 3 | click | linkText=Entrar | 
    self.driver.find_element(By.LINK_TEXT, "Entrar").click()
    # 4 | click | id=i0116 | 
    self.driver.find_element(By.ID, "i0116").click()
    # 5 | type | id=i0116 | uip.decap@policiacivil.sp.gov.br
    self.driver.find_element(By.ID, "i0116").send_keys("uip.decap@policiacivil.sp.gov.br")
    # 6 | click | id=idSIButton9 | 
    self.driver.find_element(By.ID, "idSIButton9").click()
    # 7 | mouseOver | css=.h2KSz:nth-child(4) | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".h2KSz:nth-child(4)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 8 | click | css=div:nth-child(6) .BptzE > .Idtcl | 
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6) .BptzE > .Idtcl").click()
    # 9 | click | xpath=//div[@id='AQAAAo5jsrcBAAACoc/WrwAAAAA=']/div/div/div | 
    self.driver.find_element(By.XPATH, "//div[@id=\'AQAAAo5jsrcBAAACoc/WrwAAAAA=\']/div/div/div").click()
    # 10 | mouseOver | css=#AQAAAo5jsrcBAAACoc\/WrwAAAAA\= .y1E5h | 
    element = self.driver.find_element(By.CSS_SELECTOR, "#AQAAAo5jsrcBAAACoc\\/WrwAAAAA\\= .y1E5h")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 11 | mouseOver | id=794b2300-16a8-6e9a-7c66-c76df4e1d82f | 
    element = self.driver.find_element(By.ID, "794b2300-16a8-6e9a-7c66-c76df4e1d82f")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 12 | mouseOut | id=794b2300-16a8-6e9a-7c66-c76df4e1d82f | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 13 | click | id=id__2038 | 
    self.driver.find_element(By.ID, "id__2038").click()
    # 14 | editContent | css=.dFCbN | <div style="font-family: Calibri, Arial, Helvetica, sans-serif; font-size: 12pt; color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);" class="elementToProof">Backup</div><div class="elementToProof"><div style="font-family: Calibri, Arial, Helvetica, sans-serif; font-size: 12pt; color: rgb(0, 0, 0);"><br></div><div id="Signature"><div><div><span style="font-family: Calibri, Arial, Helvetica, sans-serif; font-size: 12pt; color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);"><img src="blob:https://outlook.office365.com/6b0a4e6d-3486-41f7-868c-348e708d7c8a" style="max-width:100%" class="ContentPasted0" loadstarttime="1681839798245"><br></span></div></div></div></div><span class="_Entity _EType_OWA_VirtualEdit_Placeholder _EId_OWA_VirtualEdit_Placeholder _EReadonly_0" style="height: 21px;"><br></span>
    element = self.driver.find_element(By.CSS_SELECTOR, ".dFCbN")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<div style=\"font-family: Calibri, Arial, Helvetica, sans-serif; font-size: 12pt; color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);\" class=\"elementToProof\">Backup</div><div class=\"elementToProof\"><div style=\"font-family: Calibri, Arial, Helvetica, sans-serif; font-size: 12pt; color: rgb(0, 0, 0);\"><br></div><div id=\"Signature\"><div><div><span style=\"font-family: Calibri, Arial, Helvetica, sans-serif; font-size: 12pt; color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);\"><img src=\"blob:https://outlook.office365.com/6b0a4e6d-3486-41f7-868c-348e708d7c8a\" style=\"max-width:100%\" class=\"ContentPasted0\" loadstarttime=\"1681839798245\"><br></span></div></div></div></div><span class=\"_Entity _EType_OWA_VirtualEdit_Placeholder _EId_OWA_VirtualEdit_Placeholder _EReadonly_0\" style=\"height: 21px;\"><br></span>'}", element)
  
