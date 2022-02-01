from selenium import webdriver
from instapy import InstaPy
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.instagram.com/")
time.sleep(5)
#login = driver.find_element(By.CLASS_NAME,
login_user = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
login_user.send_keys("stop.waiting.for.friday")
time.sleep(5)
login_password = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
login_password.send_keys('djangoreinhardt123')
login_password.submit()
time.sleep(5)
search_click = driver.find_element(By.XPATH, "/html/body/div[1]/section/nav/div/div/div/div[2]/input")
search_click.send_keys('#nature')
time.sleep(10)
search_click.send_keys(Keys.ENTER)
search_click.submit()
time.sleep(120)
