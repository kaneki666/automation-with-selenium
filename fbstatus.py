from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
location = "E://chromedriver"
driver = webdriver.Chrome(location)
driver.get('https://www.facebook.com/')

email = driver.find_element_by_id('email')
email.send_keys("msadman789@gmail.com")

password =driver.find_element_by_id('pass')
password.send_keys("Kanekiken789@")

login_button = driver.find_element_by_id("u_0_a")
login_button.click()

status= driver.find_element_by_name("xhpc_message")
status.send_keys("this is written by selenium")

share = driver.find_element_by_xpath("//button[@data-testid='react-composer-post-button']")
share.click()

