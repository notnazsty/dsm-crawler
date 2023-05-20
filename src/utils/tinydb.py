from tinydb import TinyDB, Query
from src.utils.log import log
from src.utils.notifications import notify

def initialize_db():
    log(f"Initializing the databases ...")
    db = TinyDB("out/db.json")
    return db



def insert_item(db, item):
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

        ## Handle situations where the data was updated
        handle_updated_item(previous_item, item)

        return

    log("Inserting " + item['name']+ " into the database.")
    db.insert(item)



def handle_updated_item(previous_item, item):
    try:
        price_diff = previous_item["offers"][0]["price"] - item["offers"][0]["price"]
        if (price_diff > 0):
            print("PRICE DECREASED")
            log("The price of " + item['name'] + " has decreased by " + str(price_diff) + " dollars.")
            notify("PRICE CHANGE","The price of " + item['name'] + " has decreased by " + str(price_diff) + " dollars.")
    except Exception as e:
        log("An error occured while handling an updated item: " + str(e))