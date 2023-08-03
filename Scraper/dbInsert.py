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
import utils
import utils
from dotenv import load_dotenv

# parser imports
from fetchMain import fetchAndCompare
import json
# parser imports
from fetchMain import fetchAndCompare
import json




class DBINSERT:
    def __init__(self, productGroupList:dict) -> None:
        self.productList = productGroupList
        self.province_id:int
        self.searh_query:str
        self.insertedPoducts = set()
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
        self.cur.execute(''' SELECT * FROM stores WHERE merchant_id = (%s) AND merchant_storeid = (%s)
                            LIMIT 1 ;
                            ''', (merchant_id, merchant_storeid))
        store = self.cur.fetchone()

        if(store != None):
            return store[0] # return pk from store table entry
        
        self.cur.execute(''' INSERT INTO stores (merchant_id, province_id, merchant_storeid, location_name)
                             VALUES (%s, %s, %s, %s);''', (merchant_id, province_id, merchant_storeid, location_name))
        
        self.cur.execute(''' SELECT * FROM stores WHERE merchant_id = (%s) AND merchant_storeid = (%s)
                            LIMIT 1 ;
                            ''', (merchant_id, merchant_storeid))
        return self.cur.fetchone()[0] # return pk from store table entry
        
    def insert_brand(self, brand_name:str):
        self.cur.execute(''' SELECT * FROM brands WHERE brand_name = (%s)
                            LIMIT 1 ;
                            ''', (brand_name,))
        brand = self.cur.fetchone()

        if(brand != None):
            return brand[0]
        
        self.cur.execute(''' INSERT INTO brands (brand_name)
                             VALUES (%s)''', (brand_name,))
        self.cur.execute(''' SELECT * FROM brands WHERE brand_name = (%s)
                            LIMIT 1 ;
                            ''', (brand_name,))
        return self.cur.fetchone()[0]


    def get_meassurementUnit_pk(self, unit:str):
        self.cur.execute(''' SELECT * FROM meassurement_units WHERE lower(unit_name) = lower(%s)
                            LIMIT 1 ;
                            ''', (unit,))
        unit_entry = self.cur.fetchone()

        if(unit_entry != None):
            return unit_entry[0]
        else:
            return unit_entry # this returns Nonw -> throw an error from the calling function if None is returned for debudding.

    # inserts/updates a product in/to the database and returns pk after insertion or if found
    def dbInsertProduct(self, product:dict):
        name = product.get('name')
        brand = product.get('brand')
        total_price = utils.extract_decimal_value(str(product.get('total_price')))
        size_unit = product.get('size').get('unit')
        size_unit_amount = utils.extract_decimal_value(product.get('size').get('amount'))
        is_available = bool(product.get('is_available'))
        image_url = product.get('image_link')
        merchant_name = product.get('merchant')
        merchant_store_id = str(product.get('storeID'))
        merchant_store_name = '' # Modify after adding to product dict
        merchant_product_id = product.get('merchant_productId')

        # insert merchant or get merchant's pk
        merchant_pk = self.insert_merchant(merchant_name)
    
        # insert store
        store_pk = self.insert_store(merchant_pk, self.province_id, merchant_store_id, merchant_store_name)
                
        # check if product in db
        self.cur.execute(''' SELECT * FROM products WHERE lower(product_name) = lower(%s) 
                             AND merchant_productid = (%s) AND store_id = (%s)
                             LIMIT 1''', (name, merchant_product_id, store_pk))
        product_selectResult = self.cur.fetchone()
        
        if(product_selectResult != None):
            # check is product was already inserted/updated in this session
            product_pk = int(product_selectResult[0])
            if(product_pk in self.insertedPoducts):
                return
            
            self.insertedPoducts.add(product_pk)
            self.cur.execute(''' UPDATE products SET total_price = (%s)
                                 WHERE product_id = (%s)''', (total_price, product_pk)) # CODE TO UPDATE THE total_price column value of the entry
            return product_pk
        
     

        # insert brand
        brand_pk = self.insert_brand(brand)

        # get pk of meassurement unit
        meassurementUnit_pk = self.get_meassurementUnit_pk(size_unit)
        if(meassurementUnit_pk == None):
            raise ValueError(f'''unit {size_unit} is not available in the db. Please insert this unit into the 'meassurement_units' table or correct the unit in the parser.\n\nproduct: {product}
                                ''')
        
        # insert statement for prodcut 
        self.cur.execute(''' INSERT INTO products (product_name, total_price, size_amount, store_id, is_available, image_url, merchant_productid, brand_id, size_unit)
                             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)''', (name, total_price, size_unit_amount, store_pk, is_available, 
                                                                              image_url, merchant_product_id, brand_pk, meassurementUnit_pk))

        self.cur.execute(''' SELECT * FROM PRODUCTS
                                 ORDER BY product_id DESC''')
        product_pk = int(self.cur.fetchone()[0])

    def insert_group(search_query:str):
        pass
        
    def dbInsertGroups(self) -> None:
        self.province_id = self.productList.get('province_id')
        self.searh_query = self.productList.get('search_query')
        groups = self.productList.get('groups')
        for grp in groups:
            groupID = grp.get('groupID')
            products = grp.get('products')
            # insert group and get pk of group to be used in the for loop
            for prod in products:
                prod_pk = self.dbInsertProduct(prod)
                 # insert into the product_groupings table
        
    def dbInsertGroups(self) -> None:
        self.province_id = self.productList.get('province_id')
        self.searh_query = self.productList.get('search_query')
        groups = self.productList.get('groups')
        for grp in groups:
            groupID = grp.get('groupID')
            products = grp.get('products')
            # insert group and get pk of group to be used in the for loop
            for prod in products:
                prod_pk = self.dbInsertProduct(prod)
                 # insert into the product_groupings table

    def __del__(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()
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
if __name__ == '__main__':
    # uncommment line below to run the fethc and parsers - commented to skip this for debuggin
    # productList = fetchAndCompare('milk')
    with open('matchedGroups.json') as json_file:
        productList = json.load(json_file)
    dbInsert = DBINSERT(productList)
    dbInsert.connect()
    dbInsert.dbInsertGroups()


