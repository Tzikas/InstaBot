from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
from configparser import ConfigParser

class InstaBot:
    def __init__(self,username,password):

        '''
        Initializes an instance of the InstaBot class.

        Call the login methodto authenticate a user with IG.

        Args:
            username: str: The IG username for user.
            password: str: The IG password for user.
        '''
        self.username = username
        self.password = password
        # chromedriver = r'C:\Users\chaba\documents\code\python\InstaBotFolder' #Previously '/usr/local/bin/chromedriver'
        self.base_url=('https://www.instagram.com')
        self.browser = webdriver.Chrome(executable_path = r'C:\Code\Code Stuff\chromedriver')
        self.login()
        
    def login(self):
        
        self.browser.get('{}/accounts/login/'.format(self.base_url))
        time.sleep(3)
        self.browser.find_element_by_name('username').send_keys(self.username)
        self.browser.find_element_by_name('password').send_keys(self.password)
        time.sleep(3)
        self.browser.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()

    def nav_user(self,user):
        self.browser.get('{}/{}/'.format(self.base_url, user))

    def follow_user(self, user):
        self.nav_user(user)
        follow_button = self.browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/div/span/span[1]/button')

if __name__ == '__main__':

    parser = ConfigParser()
    parser.read('credentials.ini')
    usr = parser.get('igCredentials','usr')
    pwd = parser.get('igCredentials','pwd')

    
    ig_bot = InstaBot(usr,pwd)
    time.sleep(2)
    ig_bot.follow_user('marvel')

#https://youtu.be/7qcQDeShXpg?t=2452 link where you left off