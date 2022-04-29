from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pandas as pd
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.n11.com/bilgisayar/dizustu-bilgisayar?pg=2")
driver.maximize_window()

product_links = []
cacheLinks=[]

i = 0
while i < 40:
    next_link = driver.find_element(By.XPATH,'//*[@id="contentListing"]/div/div/div[1]/div[5]/a[@class="next navigation"]')
    cacheLinks = driver.find_elements(By.XPATH,'//*[@id="view"]/ul/li/div/div[@class="pro"]//a[@href]')
    for p in range(28):
        try:
            print(cacheLinks[p].get_attribute('href'))
        except:
            print("hata")
    print("-----------------------------")
    next_link.click()
    i+=1


df_links=pd.DataFrame(columns=['Links'])


        


def test():
    for p in cacheLinks:
        p.click()      
        #print(p.get_attribute('href'))
        #driver.get(p.get_attribute('href'))
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="unf-prop"]/div/p/span').click()
        product_page_details = driver.find_elements(By.XPATH,'//*[@id="unf-prop"]/div/ul/li')
        #print(product_page_details)
        for d in product_page_details:
            print(d.text)
        driver.back()


products = []