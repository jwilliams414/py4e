import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
service_obj = Service(r'C:\Users\wjennifer\AppData\Local\Programs\Python\Python39\Lib\site-packages\chromedriver_py\chromedriver_win32.exe')
driver = webdriver.Chrome(options=options,service=service_obj)
driver.get("https://fruitshoppe.firebaseapp.com")
driver.implicitly_wait(5)

from selenium.webdriver.common.by import By
#Find Mangocados on the screen using it's xpath value and then click on it
fruitfromhomepage = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div[1]/div/div/a")
fruitfromhomepage.click()
#print(fruitfromhomepage)
#The click loads the Market, click on Bananas - find bananas on the screen using its xpath
fruitfrommarketpage = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div[1]/div/div[3]/div/div[2]/a")
fruitfrommarketpage.click()
#print (fruitfrommarketpage)
#Find the cart button by using it's xpath and then click on it
cart = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/a[3]/span[1]")
cart.click()
#print(cart)
#Find the values of both fruits in the cart using xpath
fruitincart = (driver.find_element(By.XPATH, "/html/body/div[3]/div/div/ul/li[2]/div/div[1]").text)
print (fruitincart)
secondfruitincart = (driver.find_element(By.XPATH, "/html/body/div[3]/div/div/ul/li[3]/div/div[1]").text)
print (secondfruitincart)
#Ensure the text values of the fruits match what was added to the cart and then deliever a success message
if (fruitincart == 'Mangocados') and (secondfruitincart == 'Bananas'):
    print ('Yay! Capture script correctly captured both fruits added to the cart')
