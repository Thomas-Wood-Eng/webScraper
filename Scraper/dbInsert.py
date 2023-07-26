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
        
        self.cur.execute(''' INSERT INTO sotres (merchant_id, province_id, merchant_storeid, location_name)
                             VALUES (%s, %s, %s, %s);''', (merchant_id, province_id, merchant_storeid, location_name))
        
        self.cur.execute(''' SELECT * FROM stores WHERE merchant_id = (%s) AND merchant_storeid = (%s)
                            LIMIT 1 ;
                            ''', (merchant_id, merchant_storeid))
        return self.cur.fetchone()[0]
        
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
                             AND merchant_productid = (%s)
                             LIMIT 1''', (name, merchant_product_id))
        product_selectResult = self.cur.fetchone()
        
        if(product_selectResult != None):
            # check is product was already inserted/updated in this session
            if(product_selectResult[0] in self.insertedPoducts):
                return
            else:
                self.insert_store.add(product_selectResult[0])

            # if product already exisits, update the total_price column value
            self.cur.execute() # CODE TO UPDATE THE total_price column value of the entry
            return
        
     
        # insert merchant or get merchant's pk
        merchant_pk = self.insert_merchant(merchant_name)
    
        # insert store
        store_pk = self.insert_store(1, 2, "1077", 'GRANDVIEW - VANCOUVER')

        # insert brand
        brand_pk = self.insert_brand(brand)

        # get pk of meassurement unit
        meassurementUnit_pk = self.get_meassurementUnit_pk(size_unit)
        if(meassurementUnit_pk == None):
            raise ValueError(f'''unit {size_unit} is not available in the db. Please insert this unit into the 'meassurement_units' table or correct the unit in the parser.\n\nproduct: {product}
                                ''')
        # insert staqtement for prodcut 

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


