from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.remote_connection import LOGGER
from utils import priceParser
import time
import requests
from bs4 import BeautifulSoup
import csv
import logging



LOGGER.setLevel(logging.WARNING)

options = Options()
options.headless = False

driver = webdriver.Chrome(options=options)

website = "https://voila.ca/"

def web_scrape(website, good):
    r = requests.get(website)

    soup = BeautifulSoup(r.content, 'html5lib')

    items = []

    table = soup.find('div', attrs={'data-synthetics': 'product-list'})

    excluded_properties = ['base__Card-sc-1mnb0pd-4 layout__Placeholder-sc-nb1ebc-1 jIjNlL gjEHMv']

    child_divs = []

    for div in table.find_all('div', recursive=False):
        if not any(prop in div.get('class', []) for prop in excluded_properties):
            child_divs.append(div)

    for product in child_divs:
        item = {}
        for title in product.findAll('div', attrs={'data-test': 'fop-body'}):
            item['Name'] = title.h3.text

        for price in product.findAll('div', attrs={'data-test': 'fop-price-wrapper'}):
            item['Price'] = priceParser(price.strong.text)

        if(len(item) == 2):
            items.append(item)

    return items


def safeway_main(item):
    search_product(website, item)
    items = web_scrape(driver.current_url, item)
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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    safeway_main("Bread")