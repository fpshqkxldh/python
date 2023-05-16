# 셀레니움

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.naver.com")

# 잠깐 켜졌다 꺼지는 것을 멈추기
time.sleep(5)

# 네이버에서 뉴스가 있는 위치(해당 텍스트에서 마우스 우클릭 -> 검사 -> 해당 코드에서 우클릭
# -> copy -> copy full xpath)
# /html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[2]/li[2]/a
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[2]/li[2]/a").click()
time.sleep(3)

newstitle = driver.find_element(By.XPATH, "/html/body/div[2]/div/section[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/a/div[2]/div").text
print(newstitle)
