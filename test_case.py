
#coding=utf-8
from selenium import webdriver
import time

def login():
    mydriver.switch_to.frame(mydriver.find_element_by_id('x-URS-iframe'))
    time.sleep(1)
    mydriver.find_element_by_xpath("//input[@name='email']").clear()
    mydriver.find_element_by_xpath("//input[@name='email']").send_keys('hotpsy')
    time.sleep(1)
    mydriver.find_element_by_xpath("//form[@id='login-form']//div[@class='m-container']//input[@name='password']").send_keys("Aa13033615658")
    mydriver.find_element_by_xpath("//form[@id='login-form']//div[@class='m-container']//div[@class='f-cb loginbox']/a").click()

def logout():
    mydriver.switch_to.default_content()  # ����Ҫ  ����frame���
    mydriver.find_element_by_link_text("�˳�").click()
    time.sleep(5)
    mydriver.quit()


mydriver=webdriver.Firefox()
mydriver.get("http://mail.126.com/")
time.sleep(3)
print mydriver.title
print mydriver.current_url

login()
time.sleep(3)
logout()