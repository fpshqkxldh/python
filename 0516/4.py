# 주식 관련 정보 수집하기

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://finance.naver.com/")
time.sleep(3)

list1 = []
juga1 = []
for i in range(10) :
    event = driver.find_element(By.XPATH, f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/th").text
    list1.append(event)
    for j in range(3) :
        juga = driver.find_element(By.XPATH, f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/td[{j+1}]").text
        juga1.append(juga)

print(list1)
print(juga1)