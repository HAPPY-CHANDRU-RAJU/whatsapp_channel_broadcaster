from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
driver.set_window_size(1440, 876)
print("Scan QR Code, And then Enter")
input()
print("Logged In")
time.sleep(5)

driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div[4]/header/div[2]/div/span/div[3]/div/span").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div[3]/div/span/div/span/div/div/div/div/div/div/div/div/div/div/div/div").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@id=\'main\']/footer/div/div/span[2]/div/div[2]/div/div/div/p").click()
time.sleep(2)

message_box = driver.find_element(By.XPATH, "//div[@id=\'main\']/footer/div/div/span[2]/div/div[2]/div/div/div")
message = 'Hello, this is a test message from Python!'
message_box.send_keys(message)
message_box.send_keys(Keys.ENTER)  

time.sleep(10)

input()
print("Done")
time.sleep(10)
driver.quit()