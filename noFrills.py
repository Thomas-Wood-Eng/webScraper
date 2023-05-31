from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import csv

driver = webdriver.Chrome()

# change item list to get ~50 responses per search
groceries = [
    "White bread",
    "Eggs",
]

website = "https://www.nofrills.ca/"

def web_scrape(website, good):
    #r = requests.get(website)

    soup = BeautifulSoup(website, 'html5lib')

    print(website)

    items = []

    table = soup.find('ul', attrs={'data-cruller': 'product-tile-group'})

    # excluded_properties = ['base__Card-sc-1mnb0pd-4 layout__Placeholder-sc-nb1ebc-1 jIjNlL gjEHMv']

    # print(table)

    child_divs = []

    for div in table.find_all('li', recursive=False):
        #if not any(prop in div.get('class', []) for prop in excluded_properties):
        child_divs.append(div)

    for product in child_divs:

        # print(product)

        item = {}
        for title in product.findAll('div', attrs={'class': 'product-tile__details__info'}):
            item['Name'] = title.h3.text

        for price in product.findAll('span', attrs={'class': 'price selling-price-list__item__price selling-price-list__item__price--now-price'}):
            item['Price'] = price.span.text

        items.append(item)

    filename = good + '2.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f, ['Name', 'Price'])
        w.writeheader()
        for item in items:
            if 'Name' in item and 'Price' in item:
                w.writerow(item)


def main():
    for item in groceries:
        search_product(website, item)
        web_scrape(driver.page_source, item)

    driver.quit()

def search_product(store_url, product_keywords):


    driver.switch_to.new_window('tab')
    driver.get(store_url)

    search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "input")))

    search_bar.click()
    search_bar.clear()
    search_bar.send_keys(product_keywords)
    search_bar.send_keys(Keys.RETURN)

    time.sleep(5)

    #wait = WebDriverWait(driver, 10)
    #dynamic_content = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.dynamic-content")))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()