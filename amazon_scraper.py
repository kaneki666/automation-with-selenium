from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
location = "E://chromedriver"
driver = webdriver.Chrome(location)
driver.get('https://www.amazon.com/')
textsearch = "Oneplus 7t"

time.sleep(2)

info = []

search = driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
search.send_keys(textsearch)
search.find_element_by_xpath("//input[@class='nav-input']").click()
time.sleep(2)
for name in driver.find_elements_by_class_name("a-size-base-plus"):
    info.append(name.text)

for price in driver.find_elements_by_class_name('a-color-base'):
	info.append(price.text)

print(info)
