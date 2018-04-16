from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import re
import datetime
from difflib import SequenceMatcher
from random import randint

global browser
global element


# Function to scroll and click an element passed into it
def scrollclick(element):
    # scrolls until the element is in view, and clicks
    try:
        element.click()
    except NoSuchElementException:
        browser.execute_script("return arguments[0].scrollIntoView();", element)
        element.click()
    return


# Function to scroll so that a particular element is in view
def scroll(element):
    # scrolls until element is in view
    try:
        browser.execute_script("return arguments[0].scrollIntoView();", element)
        return
    except NoSuchElementException:
        # do some error handling
        print("Error handle")


# main script
# opens browser and gets to the correct landing page
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Change this path to your relevant chromedriver path
browser = webdriver.Chrome("/home/nick/PycharmProjects/Evan_demo/chromedriver", chrome_options=options)

url = "http://regaliashop.es/admin945fg3h1k/index.php?controller=AdminLogin&token=e4b8e489175d93edc06c84544e5addb3"
browser.get(url)
time.sleep(1)

# Login
elem = browser.find_element(By.NAME, "email")
elem.clear()
elem.send_keys("blah")
time.sleep(2)
elem = browser.find_element(By.NAME, "passwd")
elem.clear()
elem.send_keys("Blah")
time.sleep(4)

elem = browser.find_element(By.NAME, "submitLogin")

# browser.close()