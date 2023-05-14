
from src.scraping.links import get_individual_item_info, get_item_links, scrape_items
from src.utils.log import log
from src.utils.tinydb import initialize_db





def main():

    db = initialize_db()

    scrape_items(db)

    # log("Starting up DSM Crawler...")

    # try:
    #     # Check to see if we have item links already stored
    #     # If we do, we can just use those instead of scraping again
    #     # TODO: Add a check to see if the links are still valid
    #     # If they are, we can just use those instead of scraping again

    #     #IF NEEDED Grab the item links

    #     items_links = get_item_links()
    #     write_item_links_to_csv(items_links)

    #     # Initialize the database


    # except IndexError as e:
    #     log("An Error has occured: " + str(e) + ", the scraper is now shutting down.")


    # log("DSM Crawler has shut down.")





if __name__ == '__main__':
    main()