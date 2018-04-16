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

url = "http://www.bbc.co.uk"
browser.get(url)
if browser.title == 'BBC - Home':
    time.sleep(2)
    print("Success")

# Find top story
elem = browser.find_element(By.CLASS_NAME, "top-story__title")

# Click on top story
scrollclick(elem)
time.sleep(2)

# Print title and headline
print(browser.title)

headline = browser.find_element_by_class_name("story-body__h1")
print(headline.text)


# Find most popular story
mp = browser.find_elements_by_class_name("most-popular-list-item__headline")

for m in mp:
    print(m.text)

browser.close()