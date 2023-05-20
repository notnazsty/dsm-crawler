from src.scraping.links import  get_item_links, scrape_items
from src.utils.log import log
from src.utils.tinydb import initialize_db
from src.utils.read import read_file_as_df
from src.utils.write import write_item_links_to_csv
from src.utils.notifications import notify


RE_FETCH_ITEM_LINKS = False
REFRESH_PRODUCT_INFO_TIME = 60 * 60  # 1 hour

def main():
    db = initialize_db()

    log("Starting up DSM Crawler...")
    notify("DSM Crawler has started up.","")
    try:

        item_link_df = read_file_as_df('out/item_links.csv')

        items_links = []

        if item_link_df.shape[1] == 0 or RE_FETCH_ITEM_LINKS:
            items_links = get_item_links()
            write_item_links_to_csv(items_links)
            item_link_df = read_file_as_df('out/item_links.csv')
        else:
            log("Item links already exist, skipping item link scraping.")

        scrape_items(item_link_df, db)


        ## Update Loop Run A Callback Every X Seconds
            ## run a data_analysis function to display the new data


    except IndexError as e:
        log("An Error has occured: " + str(e) + ", the scraper is now shutting down.")


    log("DSM Crawler has shut down.")
    notify("DSM Crawler has started up.","")





if __name__ == '__main__':
    main()