from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
import time

start_time = time.time()
driver = webdriver.Chrome(executable_path= "chromedriver.exe")

driver.get("https://clever.com/oauth/ldap/login?target=NTdiMzYwYjIxNDJhNWIwMTAwMDAwYzAy;NGM2M2MxY2Y2MjNkY2U4MmNhYWM=;aHR0cHM6Ly9jbGV2ZXIuY29tL2luL2F1dGhfY2FsbGJhY2s=;ZDBmMWY3NjQ2MmJlYzE0MjA4MzQzNTc3OWMzZjYwYzdjMGE0MjUwNmU0ZTNmYTk5Yjg2NzhlMzZjZWRlMjcxMg==;Y29kZQ==;")

f = open("config.txt","r")
lines = f.readlines()
user = lines[0]
loginPass = lines[1]
firstClass = lines[2]
secondClass = lines[3]
f.close()

LDAP = driver.find_element(By.XPATH, "//a[@aria-label='Log in with LDAP']")
LDAP.click()
driver.implicitly_wait(5)

username = driver.find_element(By.XPATH, "//input[@id='username']")
username.send_keys(user)

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(loginPass)


driver.implicitly_wait(5)

flexischediButton = driver.find_element(By.XPATH, "//div[6]//div[2]//div[7]//a[1]")
flexischediButton.click()


driver.switch_to.window(driver.window_handles[1])

flexischedLogin = driver.find_element(By.XPATH, "//div[@class='img-padding']")
flexischedLogin.click()



class1 = driver.find_element(By.XPATH, "//div[@class='dataTables_scrollHead']//th[3]//input[1]")
class1.send_keys(firstClass)

driver.implicitly_wait(5)
class1Confirm = driver.find_element(By.XPATH, "//body[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[3]")
class1Confirm.click()

alert1 = driver.switch_to.alert
time.sleep(1)
driver.implicitly_wait(5)
time.sleep(1)
alert1.accept()
time.sleep(1)
driver.implicitly_wait(5)
alert1.accept()

class2 = driver.find_element(By.XPATH, "//div[@class='dataTables_scrollHead']//th[4]//input[1]")
class2.send_keys(secondClass)

class2Confirm = driver.find_element(By.XPATH, "//body[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[4]")
class2Confirm.click()

alert2 = driver.switch_to.alert
driver.implicitly_wait(5)
time.sleep(1)
alert2.accept()
time.sleep(1)
driver.implicitly_wait(5)
alert2.accept()
time.sleep(5)

print("You have been succesfully scheduled for " + firstClass + " on Tuesday and " + secondClass + " on Wednesday.")
