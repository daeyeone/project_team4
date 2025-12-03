import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


url = "https://play.google.com/store/apps/details?id=sudoku.puzzle.free.game.brain"
driver.get(url)
time.sleep(3)


review_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label*='평점 및 리뷰 자세히 알아보기']")
review_button.click()
time.sleep(3)


sort_button = driver.find_element(By.XPATH, "//*[@id='sortBy_1']/div[2]/i")
sort_button.click()
time.sleep(5)

latest_option = driver.find_element(By.CSS_SELECTOR, "span[aria-label='최신']")
driver.execute_script("arguments[0].click();", latest_option)
time.sleep(2)





