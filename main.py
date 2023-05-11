
from src.scraping.links import get_item_links
from src.utils.write import write_array_to_text_file, write_item_links_to_csv




items_links = get_item_links()
write_item_links_to_csv(items_links)


