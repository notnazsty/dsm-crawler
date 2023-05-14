from bs4 import BeautifulSoup
import requests

from src.utils.read import read_file
from src.utils.log import log

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
        response = requests.get('https://shop-us.doverstreetmarket.com/collections/' + brand)
        soup = BeautifulSoup(response.text, 'html.parser')

        # TODO if I really wanna grab everything I should use Selenium to scroll all the way down so that every item can load

        log("searching for anchor tags with " + f"a[href^='/collections/{brand}/products']")
        items = soup.select(f'a[href^="/collections/{brand}/products"]')
        log("Found " + str(items.__len__()) + " items associated with " + brand)
        for item in items:
            item_name = item['href'].replace("/collections/aarahee/products/","")
            item_links.append((brand,item_name,'https://shop-us.doverstreetmarket.com/' + item["href"]))

    return item_links

    

