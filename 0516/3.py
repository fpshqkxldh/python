# 아파트 시세 크롤링

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://m.land.naver.com/search")
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").click()
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").send_keys("잠원동 반포센트럴자이")
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/button[2]/i").click()
time.sleep(3)

salesprice = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[1]/dd").text
jeonse = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[2]/dd").text

print("< 잠원동 반포센트럴자이 시세 >")
print("매매가 : ", salesprice)
print("전세가 : ", jeonse)