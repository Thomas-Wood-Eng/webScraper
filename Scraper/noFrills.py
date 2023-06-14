from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from utils import priceParser
import time
import requests
from bs4 import BeautifulSoup
import csv

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)

website = "https://www.nofrills.ca/"

def web_scrape(website, good):

    soup = BeautifulSoup(website, 'html5lib')

    items = []

    table = soup.find('ul', attrs={'data-cruller': 'product-tile-group'})

    child_divs = []

    for div in table.find_all('li', recursive=False):
        child_divs.append(div)

    for product in child_divs:
        item = {}
        for title in product.findAll('div', attrs={'class': 'product-tile__details__info'}):
            item['Name'] = title.h3.text

        for price in product.findAll('span', attrs={'class': 'price selling-price-list__item__price selling-price-list__item__price--now-price'}):
            item['Price'] = priceParser(price.span.text)

        if(len(item) == 2):
            items.append(item)

    return items

def noFrills_main(item):
    search_product(website, item)
    items = web_scrape(driver.page_source, item)

    driver.quit()
    return items

def search_product(store_url, product_keywords):


    driver.switch_to.new_window('tab')
    driver.get(store_url)

    search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "input")))

    search_bar.click()
    search_bar.clear()
    search_bar.send_keys(product_keywords)
    search_bar.send_keys(Keys.RETURN)

    time.sleep(5)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    noFrills_main("White Bread")
