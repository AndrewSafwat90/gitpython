from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

my_service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=my_service)

browser.get("https://elzero.org/")
# time.sleep(3)

search_input = browser.find_element(By.CSS_SELECTOR, 'input[type="search"]')
search_input.clear()
search_input.send_keys("Python Developer")
browser.implicitly_wait(1)
search_button = browser.find_element(
    By.CSS_SELECTOR, 'input[type="submit"]')
search_button.click()

# browser.implicitly_wait(20)
# checkbox = browser.find_element(
#     By.CSS_SELECTOR, 'input[type="checkbox"]')
# checkbox.click()

# browser.implicitly_wait(20)
# checkbox = browser.find_element(
#     By.CSS_SELECTOR, 'input[type="checkbox"]')
# checkbox.click()


input("Press Enter to close the browser...")
