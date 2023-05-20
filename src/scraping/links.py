from bs4 import BeautifulSoup
import requests
import json 

from src.utils.log import log
from src.utils.read import read_file_as_df
from src.utils.tinydb import insert_item



def get_brand_links():
    print("Attempting to get links for the brands on DSM...")
    log("Sending a request to https://shop-us.doverstreetmarket.com/collections")
    response = requests.get("https://shop-us.doverstreetmarket.com/collections")
    soup = BeautifulSoup(response.text, 'html.parser')

    brand_links = []

    headings = soup.find_all('h2', {'class': 'col-span-full sm:col-span-2 text-lg sm:text-2xl'})

    log("Found " + str(headings.__len__() )+ " brands. Getting all associated links.")

    for heading in headings:
        letter_container = heading.parent

        for link in letter_container.find_all('a'):
            brand_links.append(link['href'].replace("/collections/", ""))
    
    return brand_links


def get_item_links(): 

    brand_links = get_brand_links()

    item_links = []

    for brand in brand_links:
        log("Getting item links for " + brand)
        response = requests.get('https://shop-us.doverstreetmarket.com/collections' + brand)
        soup = BeautifulSoup(response.text, 'html.parser')

        # TODO if I really wanna grab everything I should use Selenium to scroll all the way down so that every item can load

        log("searching for anchor tags with " + f"a[href^='/collections/{brand}/products']")
        items = soup.select(f'a[href^="/collections/{brand}/products"]')
        log("Found " + str(items.__len__()) + " items associated with " + brand)
        for item in items:
            item_name = item['href'].replace(f"/collections/{brand}/products/","")
            item_links.append((brand,item_name,'https://shop-us.doverstreetmarket.com/' + item["href"]))

    return item_links

def get_individual_item_info(item_link):
    response = requests.get(item_link)
    soup = BeautifulSoup(response.text, 'html.parser')

    json_ld_tags = soup.find_all('script', {'type': 'application/ld+json'})

    for tag in json_ld_tags:
        try:
            current_tag = json.loads(tag.string)

            if (current_tag['@type'] == 'Product'): 
                return normalize_json_data(current_tag)
        except Exception as e:
            log("An error occured while trying to parse the JSON data for " + item_link + ". The error was: " + str(e)) 
            log("The JSON data was: " + json.dumps(current_tag))
            return None
        
def normalize_json_data(json_data):
    normalized_data = {}

    normalized_data['name'] = json_data['name']
    normalized_data['description'] = json_data['description']
    normalized_data['image'] = json_data['image']
    normalized_data['brand'] = json_data['brand']['name']
    normalized_data['offers'] = json_data['offers']
    normalized_data['url'] = json_data['url']
    normalized_data['sku'] = json_data['sku']

    json_str = json.dumps(json_data, sort_keys=True)
    json_hash = hash(json_str)

    normalized_data["hash"] = json_hash
    return normalized_data

def scrape_items(item_link_df,db): 
    item_links = item_link_df['Link'].to_list()[1:]

    log("Starting to extract data from " + str(item_links.__len__()) + " items.")
    for i in range(len(item_links)):
       link = item_links[i]
       data = get_individual_item_info(link)

       if (i % 10 == 0 or i == len(item_links) - 1):
            log("Extracted data from " + str(i) + " items so far.")

       if (data is not None):
           insert_item(db,data)
