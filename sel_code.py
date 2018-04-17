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
import requests


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


def browser_setup():
    # main script
    # opens browser and gets to the correct landing page
    global browser
    global element

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # Change this path to your relevant chromedriver path
    browser = webdriver.Chrome("/home/nick/PycharmProjects/Evan_demo/chromedriver", chrome_options=options)

    url = "http://regaliashop.es/admin945fg3h1k/index.php?controller=AdminLogin&token=e4b8e489175d93edc06c84544e5addb3"
    browser.get(url)
    time.sleep(1)


def login():
    # Login
    elem = browser.find_element(By.NAME, "email")
    elem.clear()
    elem.send_keys()
    time.sleep(2)
    elem = browser.find_element(By.NAME, "passwd")
    elem.clear()
    elem.send_keys()
    time.sleep(4)
    elem = browser.find_element(By.NAME, "submitLogin")
    scrollclick(elem)
    time.sleep(5)

    # Import CSV section
    url = 'http://regaliashop.es/admin945fg3h1k/index.php?controller=AdminImport&token=2e2961702497168112e4c3c2acb86155'
    browser.get(url)
    time.sleep(2)


def category_choice(category):
    # change category
    select = Select(browser.find_element(By.ID, "entity"))
    select.select_by_visible_text(category)
    time.sleep(2)


def import_files(file_location):
    # Change delimiters
    elem = browser.find_element(By.NAME, "separator")
    elem.clear()
    elem.send_keys(",")
    time.sleep(1)

    elem = browser.find_element(By.NAME, "multiple_value_separator")
    elem.clear()
    elem.send_keys(";")

    elem = browser.find_element(By.ID, "file")
    time.sleep(2)

    # Select file - change this path to one which works for your computer, just as an example
    elem.send_keys(file_location)
    time.sleep(3)

    # Next Page
    elem = browser.find_element(By.NAME, "submitImportFile")
    scrollclick(elem)
    time.sleep(2)

    # Cargar
    elem = browser.find_element(By.ID, "loadImportMatchs")
    scrollclick(elem)
    time.sleep(2)

    # Final import button
    elem = browser.find_element(By.NAME, "import")
    scrollclick(elem)


def browser_close():
    browser.close()
