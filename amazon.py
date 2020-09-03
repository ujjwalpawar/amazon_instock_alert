from bs4 import BeautifulSoup
from selenium import webdriver
import selenium
import time
import smtplib

sender_email="<your email>"
sender_password="<your password>"
reciver_email="<your another email>"
website_URL ="https://www.amazon.in/gp/product/B08CFZDZLB/" #This for ASUS ROG Zephyrus G14, 14" FHD 120Hz, 
#Ryzen 5 4600HS, GTX 1650 4GB GDDR6 Graphics, Gaming Laptop (8GB/512GB SSD/Windows 10/Eclipse Gray/Without Anime Matrix/1.6 Kg),


s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()


s.login(sender_email, sender_password)
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
while(True):
    driver.get(website_URL)
    username = driver.find_element_by_id("availability")
    html = driver.page_source
    soup = BeautifulSoup(html)
    table = soup.find(id='availability')
    if('Currently unavailable.' in str(table)):
        print('Out of Stock')

    else:
        print("In stock")
        message = "In stock hurry up"
        s.sendmail(sender_email,reciver_email , message)
    time.sleep(600)
    driver.refresh()
s.quit()
