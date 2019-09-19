from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

class Instagram:
	def __init__(self,username,password):
		self.username = username
		self.password = password
		self.bot = webdriver.Chrome()

	def DoStuff(self):
		bot = self.bot
		bot.get('https://www.instagram.com/accounts/login/')
		time.sleep(2)
		email = bot.find_element_by_name('username')
		password = bot.find_element_by_name('password')
		email.clear()
		password.clear()
		email.send_keys(self.username)
		password.send_keys(self.password)
		password.send_keys(Keys.RETURN)
		time.sleep(3)
		not_now = bot.find_element_by_class_name('aOOlW')
		not_now.click()
		time.sleep(3)
		comment = bot.find_element_by_class_name('Ypffh')
		comment.send_keys("SELENIUM IS FUN")
		post = bot.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[1]/div[1]/div/article[1]/div[2]/section[3]/div/form/button')
		post.send_keys(Keys.RETURN)
		heart = bot.find_element_by_class_name('dCJp8')
		heart.click()
User = Instagram('your twitter id','twitter password')
User.DoStuff()
