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
    "Milk",
    "Apples",
    "Chicken breast",
    "Spinach",
    "Cheese",
    "Ground beef",
    "Rice",
    "Tomatoes",
    "Bananas",
    "Yogurt",
    "Onions",
    "Salmon",
    "Carrots",
    "Potatoes",
    "Orange juice",
    "Strawberries",
    "Cucumber",
    "Pasta",
    "Lettuce",
    "Peanut butter",
    "Green beans",
    "Blueberries",
    "Watermelon",
    "Olive oil",
    "Almonds",
    "Grapes",
    "Avocado",
    "Cereal",
    "Broccoli",
    "Orange",
    "Lemons",
    "Honey",
    "Sliced turkey",
    "Cherries",
    "Mushrooms",
    "Bell peppers",
    "Pineapple",
    "Sausages",
    "Tofu",
    "Coconut milk",
    "Canned beans",
    "Hamburger buns",
    "Frozen peas",
    "Quinoa",
    "Greek yogurt",
    "Cottage cheese",
    "Sour cream",
    "Oatmeal",
    "Mayonnaise",
    "Salsa",
    "Parmesan cheese",
    "Bacon",
    "Cheddar cheese",
    "Ice cream",
    "Green tea",
    "Honeydew melon",
    "Dark chocolate",
    "Ground cinnamon",
    "Vanilla extract"
]

website = "https://voila.ca/"

def web_scrape(website, good):
    r = requests.get(website)

    soup = BeautifulSoup(r.content, 'html5lib')

    items = []

    table = soup.find('div', attrs={'data-synthetics': 'product-list'})

    excluded_properties = ['base__Card-sc-1mnb0pd-4 layout__Placeholder-sc-nb1ebc-1 jIjNlL gjEHMv']

    # print(table)

    child_divs = []

    for div in table.find_all('div', recursive=False):
        if not any(prop in div.get('class', []) for prop in excluded_properties):
            child_divs.append(div)

    for product in child_divs:

        # print(product)

        item = {}
        for title in product.findAll('div', attrs={'data-test': 'fop-body'}):
            item['Name'] = title.h3.text

        for price in product.findAll('div', attrs={'data-test': 'fop-price-wrapper'}):
            item['Price'] = price.strong.text

        items.append(item)

    filename = good + '.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f, ['Name', 'Price'])
        w.writeheader()
        for item in items:
            if 'Name' in item and 'Price' in item:
                w.writerow(item)


def main():
    for item in groceries:
        search_product(website, item)
        web_scrape(driver.current_url, item)

    driver.quit()

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
    main()