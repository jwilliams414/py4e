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
#Add the first listed featured fruit to the user's cart
fruitfromhomepage = driver.find_element(By.XPATH, ("//div[@class='featured-fruit-info']"))
fruitfronthomepagetext = driver.find_element(By.XPATH, ("//div[@class='featured-fruit-info']")).text
fruitfromhomepage.click()

#The click above loads the Market, here I want to click on Bananas and add it the cart
fruitfrommarketpage = driver.find_element(By.XPATH, ("//div[@class='fruit-box fruit-banans']/../../..//a[@class='btn btn-sm btn-primary cta-add-to-cart']"))
fruitfrommarketpagetext = driver.find_element(By.XPATH, ("//div[@class='fruit-box fruit-banans']/div/h3/a")).text
fruitfrommarketpage.click()

#Find the cart button by using it's xpath and the text My Cart and then click on it
cart = driver.find_element(By.XPATH, "//span[text()='My Cart']")
cart.click()

#go through the list and find the items on the page and compare to what I added to the cart
cartitems = driver.find_elements(By.XPATH, ("//ul[@class='cart-list ng-scope']/li[@class='cart-list-item ng-scope']"))
i = 1
found = 0
while i <= len(cartitems):
    fruitincart = (driver.find_element(By.XPATH, "//ul[@class='cart-list ng-scope']/li[@class='cart-list-item ng-scope']["+str(i)+"]/div/div").text)
    #print(fruitincart)
    if (fruitincart.lower() == fruitfronthomepagetext.lower()):
        found += 1
    elif (fruitincart.lower() == fruitfrommarketpagetext.lower()):
        found += 1
    i += 1
    if found == 2:
         print ('Yay! Capture script correctly captured both fruits added to the cart')
