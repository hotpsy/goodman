#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os

driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get("http://www.baidu.com")

#鼠标悬停至设置
link =driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(link).perform()


#打开搜索设置
driver.find_element_by_xpath("/html/body/div[3]/div[6]/a[1]").click()

#保存设置
driver.find_element_by_class_name("prefpanelgo").click()

#接受告警框
driver.switch_to_alert().accept()