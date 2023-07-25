'''
SCRIPT TO INSER GROUPINGS INTO A POSTGRES DATABASE
Steps:
1. check if product already existis in the db
    - query by name and store
        - if found update record
    - if not found, insert

2. Check if brand exisits
    -   if yes:
        - refer foreign key
    - if no:
        - insert new record to brands table and refer foreign key

'''

import psycopg2
import os
from dotenv import load_dotenv

# parser imports
from fetchMain import fetchAndCompare
import json




class DBINSERT:
    def __init__(self, productGroupList:list[dict]) -> None:
        self.productList = productGroupList
        load_dotenv()

    def connect(self):

        HOST = os.environ.get('PostGres_HOST_NAME')
        DBNAME = os.environ.get("PostGres_DBNAME")
        USERNAME = os.environ.get("PostGres_USERNAME")
        PASSWORD = os.environ.get("PostGres_PASSWORD")
        PORT = 5432


        self.conn = psycopg2.connect(host=HOST, dbname=DBNAME, user=USERNAME, password=PASSWORD, port=PORT)
        self.cur = self.conn.cursor()

    # inserts merchant if not in db and returns pk of entry
    def insert_merchant(self, merchantName:str):
        self.cur.execute("SELECT * FROM merchants WHERE lower(merchant_name) = lower(%s) LIMIT 1",
                         (merchantName,))
        merchant = self.cur.fetchone()
        if(merchant != None):
            return int(merchant[0])
        
        self.cur.execute('''INSERT INTO merchants (merchant_name)
                            VALUES (%s);''' , (merchantName,))
        self.cur.execute("SELECT * FROM merchants WHERE lower(merchant_name) = lower(%s) LIMIT 1",
                         (merchantName,))
        return int(self.cur.fetchone()[0]) # returns pk of merchant after insertion

    # insert store if not found and return the pk, if found return the pk without inserting     
    def insert_store(self, merchant_id:int, province_id:int, merchant_storeid:str, location_name:str):
        pass

    # inserts/updates a product in/to the database and returns pk after insertion or if found
    def dbInsertProduct(self, product:dict):
        name = product.get('name')
        brand = product.get('brand')
        total_price = float(product.get('total_price'))
        # unit_price = product.get('unit_price') - NA
        size_unit = product.get('unit')
        # size_unit_amount = product.get('unit_amount)
        is_available = product.get('is_available')
        image_link = product.get('image_link')
        merchant_name = product.get('merchant')
        merchant_store_id = product.get('storeID')
        merchant_product_id = product.get('merchant_productId')
        
        # check if product in db
        self.cur.execute(''' SELECT * FROM products WHERE lower(product_name) = lower(%s) 
                             AND merchant_product_id = (%s)
                             LIMIT 1''', (name, merchant_product_id))
        product_selectResult = self.cur.fetchone()

        if(product_selectResult != None):
            # if product already exisits, update the total_price column value

            return
        
     
        # insert merchant or get merchant's pk
        merchant_pk = self.insert_merchant(merchant_name)
    
        # insert store
        pass
           

    def dbInsertGroups(self) -> None:
        
        # insert product(s)
        product = self.productList[0].get('products')[0]
        self.dbInsertProduct(product)

        # insert group
        pass

    def __del__(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    # uncommment line below to run the fethc and parsers - commented to skip this for debuggin
    # productList = fetchAndCompare('milk')
    with open('matchedGroups.json') as json_file:
        productList = json.load(json_file)
    dbInsert = DBINSERT(productList)
    dbInsert.connect()
    dbInsert.dbInsertGroups()


