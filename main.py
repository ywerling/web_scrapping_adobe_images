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
# get images from the webpage
images = driver.find_elements(By.XPATH, "//img[@alt]")

# this part is for testing purpose only, it has to be commented out for production
for image in images:
    # print(image.get_attribute("alt"))
    # print(image.get_attribute("class"))
    print(f'{image.get_attribute("alt")}{image.get_attribute("name")}\n')

# write image titles to destination file
# UTF-8 to support unicode characters
with open(OUTPUT_DESTINATION, "w", encoding='utf-8') as output_file:
    #slicing to remove first and last images which are not relevant to the search
    for image in images[3:-3]:
        text_to_write = image.get_attribute("alt")
        if len(text_to_write) > 1:
            output_file.write(text_to_write)
            output_file.write('\n')