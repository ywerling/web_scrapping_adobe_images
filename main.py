from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ADOBE_STOCK_IMAGES_URL = "https://stock.adobe.com/"
OUTPUT_FILE = 'output/output.txt'

# SEARCH_TERM = "Nature"
search_term = input('Enter the search keywords to find images: ')

print(f'Opening Adobe page to find stock photos of {search_term}')

#ensure windows stays open
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver=webdriver.Chrome(chrome_options)
driver.get(ADOBE_STOCK_IMAGES_URL)

#allow the page to load
time.sleep(1)

search_input = driver.find_element(By.NAME,"keyword")
# search_input.send_keys(SEARCH_TERM)
search_input.send_keys(search_term)
search_input.send_keys(Keys.ENTER)