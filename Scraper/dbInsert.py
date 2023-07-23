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



# cur = conn.cursor()

# print(cur.execute('SELECT * FROM merchants'))
# rows = cur.fetchall()

# for row in rows:
#     print(row)

# conn.commit()
# cur.close()
# conn.close()

# function takes in list of products and inserts into db
# cur.execute("select * from account")

# class DBINSERT:
#     # inserts/updates a product in/to the data base
#     def dbInsertProduct(self, product:dict):
        

#     def dbInsertGroups(self, productGroupList:list[dict]) -> None:
#         pass




class DBINSERT:
    def __init__(self) -> None:
        load_dotenv()

    def connect(self):

        HOST = os.environ.get('PostGres_HOST_NAME')
        DBNAME = os.environ.get("PostGres_DBNAME")
        USERNAME = os.environ.get("PostGres_USERNAME")
        PASSWORD = os.environ.get("PostGres_PASSWORD")
        PORT = 5432


        self.conn = psycopg2.connect(host=HOST, dbname=DBNAME, user=USERNAME, password=PASSWORD, port=PORT)
        self.cur = self.conn.cursor()

    def checkExists_product(self, product:dict):
        # select by product name and if # of fetched rows >= 1, return true
        pass

    # inserts/updates a product in/to the database
    def dbInsertProduct(self, product:dict):
        # check if product in db
        if(not self.checkExists_product()):
            # code to insert
            pass
           

    def dbInsertGroups(self, productGroupList:list[dict]) -> None:
        # insert merchant

        # insert location
        
        # insert store

        # insert product(s)

        # insert group
        pass






