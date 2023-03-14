import time
from threading import Thread

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# chrome driver
service_obj=Service("/Users/kumaran/Downloads/chromedriver_win32/chromedriver.exe");  # creating service class object
driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()

print(driver.title)
print(driver.current_url)
driver.find_element(By.CLASS_NAME,"register-btn").click()
time.sleep(60)
driver.find_element(By.NAME,"email").send_keys("uk1792692@gmail.com")
time.sleep(60)






