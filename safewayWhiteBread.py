import requests
from bs4 import BeautifulSoup
import csv

URL = "https://voila.ca/products?source=navigation&sublocationId=c928da4c-1b7f-4d46-9b2d-4de152ea6df5"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

items = []

table = soup.find('div', attrs={'data-synthetics': 'product-list'})

for product in table.findAll('div',
                             attrs={
                                 'class': 'base__Wrapper-sc-1mnb0pd-6 base__FixedHeightWrapper-sc-1mnb0pd-41 gMlFiL '
                                          'jNtybn viewports-enabled-standard-fop__ViewportsEnabledFop-sc-nz4zf7-0 '
                                          'iGEpfJ'}):

    print(product)

    item = {}
    for title in product.findAll('div', attrs={'data-test': 'fop-body'}):
        item['Name'] = title.h3.text

    for price in product.findAll('div', attrs={'data-test': 'fop-price-wrapper'}):
        item['Price'] = price.strong.text

    items.append(item)

filename = 'whiteBread.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, ['Name', 'Price'])
    w.writeheader()
    for item in items:
        w.writerow(item)

