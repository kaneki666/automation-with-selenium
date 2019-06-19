from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
location = "E://chromedriver"
driver = webdriver.Chrome(location)
driver.get('https://www.facebook.com/')


firstname = driver.find_element_by_id('u_0_l')
firstname.send_keys("enter your firstname")
surname = driver.find_element_by_id('u_0_n')
surname.send_keys("enter your lastname")
email = driver.find_element_by_id('u_0_q')
email.send_keys("enter your email")
reemail = driver.find_element_by_id('u_0_t')
reemail.send_keys("enter your email")
password =driver.find_element_by_id('u_0_x')
password.send_keys("enter your password")
date = Select(driver.find_element_by_id('day'))
date.select_by_value('enter your date example 16')
date = Select(driver.find_element_by_id('enter your month example 11'))
date.select_by_value('enter your')
date = Select(driver.find_element_by_id('year'))
date.select_by_value('enter your year')
male = driver.find_element_by_id('u_0_6')
male.click()
signup = driver.find_element_by_id('u_0_15')
signup.click()






