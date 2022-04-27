from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager
import json
from selenium.webdriver.common.by import By
import time

data = []

def test_driver_manager_chrome():
    service = ChromeService(executable_path=ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service)
    driver.get('https://www.prothomalo.com/')
    title  =  driver.find_elements(By.CLASS_NAME, "news_with_no_image")
    for element in title:
        title = element.find_element(By.CLASS_NAME, "headline-title").text
        des = element.find_element(By.CLASS_NAME, "excerpt").text
        link = element.find_element(By.CLASS_NAME,'newsHeadline-m__title-link__1puEG').get_attribute('href')
        obj = {
            "title":title,
            "des":des,
            "link":link
        }
        data.append(obj)
  
test_driver_manager_chrome()
with open("sample.json",  'w', encoding='utf8') as outfile:
    json.dump(data, outfile,ensure_ascii=False)
print(data)
