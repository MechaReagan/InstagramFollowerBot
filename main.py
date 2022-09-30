from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

INSTA_ACCOUNT = input("Which Instagram account would you like to follow the followers of?\n")
CHROME_DRIVER_PATH = r"C:\Users\gorem\OneDrive\Documents\chromedriver_win32\chromedriver.exe"
USERNAME = os.environ.get("username")
PASSWORD = os.environ.get("password")
ser = Service(CHROME_DRIVER_PATH)


class InstaFollower():

    def __init__(self):
        self.driver = webdriver.Chrome(service=ser)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        email = self.driver.find_element(By.CSS_SELECTOR, ".f0n8F input")
        email.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        time.sleep(1)
        log_in = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
        log_in.click()
        time.sleep(4)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{INSTA_ACCOUNT}/")
        time.sleep(3)
        followercount = self.driver.find_element(By.CSS_SELECTOR, ".qi72231t")
        followercount.click()
        time.sleep(2)
        scr1 = self.driver.find_element(By.CSS_SELECTOR, '._aano')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
            time.sleep(2)

    def follow(self):
        following = self.driver.find_elements(By.CSS_SELECTOR, "._aano button")
        for follow in following:
            follow.click()
            time.sleep(1)


bot = InstaFollower()

bot.login()
bot.find_followers()
bot.follow()