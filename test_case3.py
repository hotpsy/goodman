#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os

driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get("http://www.baidu.com")

#�����ͣ������
link =driver.find_element_by_link_text("����")
ActionChains(driver).move_to_element(link).perform()


#����������
driver.find_element_by_xpath("/html/body/div[3]/div[6]/a[1]").click()

#��������
driver.find_element_by_class_name("prefpanelgo").click()

#���ܸ澯��
driver.switch_to_alert().accept()