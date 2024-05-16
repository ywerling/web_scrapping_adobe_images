from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ADOBE_STOCK_IMAGES_URL = "https://stock.adobe.com/"
OUTPUT_DESTINATION = 'output.txt'

# SEARCH_TERM = "Nature"
search_term = input('Enter the search keywords to find images: ')

print(f'Opening Adobe page to find stock photos of {search_term}')

#ensure windows stays open
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver=webdriver.Chrome(chrome_options)
driver.get(ADOBE_STOCK_IMAGES_URL)

# allow the page to load
time.sleep(1)

search_input = driver.find_element(By.NAME,"keyword")
# search_input.send_keys(SEARCH_TERM)
search_input.send_keys(search_term)
search_input.send_keys(Keys.ENTER)

# allow the page to load
time.sleep(1)

# images = driver.find_elements(By.CSS_SELECTOR, "#js-img-protect alt")
images = driver.find_elements(By.XPATH, "//img[@alt]")
for image in images:
    # print(image.get_attribute("alt"))
    # print(image.get_attribute("class"))
    print(f'{image.get_attribute("alt")}{image.get_attribute("class")}\n')

with open(OUTPUT_DESTINATION, "w", encoding='utf-8') as output_file:
    for image in images:
        text_to_write = image.get_attribute("alt")
        output_file.write(text_to_write)
        output_file.write('\n')