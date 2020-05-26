# -*- coding: utf-8 -*-
"""
Created on Mon May 18 01:23:36 2020

@author: verma
"""


from selenium import webdriver
import time
import os

cwd = os.chdir(r"C:\Users\verma\Udemy\ZerodhaKiteConnect")
def autologin():
    print("Running tinder.py")
    time.sleep(1)
    print("Starting webdriver.chrome.service.Service" )
    time.sleep(2)
    service = webdriver.chrome.service.Service(r'C:\Users\verma\chromedriver_win32/chromedriver.exe')
    service.start()
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    options.add_argument('user-data-dir=F:/User Data1/')
    options = options.to_capabilities()
    time.sleep(5)
    driver = webdriver.Remote(service.service_url, options)
    driver.get("https://www.selenium.dev/")
    time.sleep(5)
    driver.implicitly_wait(25)
    driver.get("https://tinder.com/app/profile")
    driver.implicitly_wait(125)
    time.sleep(3)
    #Using xpaths
    driver.implicitly_wait(25)
    driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/aside/div/div/a').click()
    
    for i in range(1,50):
        driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button').click()
        time.sleep(0.1)

    driver.quit()
    password="prnvat8197"
    username=driver.find_element_by_xpath('//*[@id="identifierId"]')
    username.send_keys("pranav.atulya@gmail.com")
    print("Matches found: 0")
    print("\n""\n")
    time.sleep(5)
    print("lmao, you gonna die alone.")
    
    
    
autologin()