#coding = utf-8
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as ec
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(5)
print(ec.title_contains("9999"))