from tinydb import TinyDB, Query
from src.utils.log import log

def initialize_db():
    log("Initializing the database...")
    db = TinyDB('out/db.json')
    return db


def insert_item(db,item):
    Entries = Query()
    if (db is None):
        log("The database is not initialized. Please call initialize_db() before inserting items.")
        return
    
    search_res = db.search(Entries.name == item['name'])

    if (search_res.__len__() > 0):

        ## DO A COMPARISON & THEN UPDATE THE VALUE IF ITS DIFFERENT
        previous_item = search_res[0]

        if previous_item["hash"] == item["hash"]:
            log("Item " + item['name'] + " already exists in the database. No changes were made.")
            return


        log("Item " + item['name'] + " already exists in the database. Updating the entry.")
        db.update(item, Entries.name == item['name'])

        
        print("UPDATED A VALUE")
        ## Handle situations where the data was updates

        return

    log("Inserting " + item['name']+ " into the database.")
    db.insert(item)
