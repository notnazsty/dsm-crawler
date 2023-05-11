from bs4 import BeautifulSoup
import requests
import json

from src.utils.read import read_file


def get_brand_links():
    response = requests.get("https://shop-us.doverstreetmarket.com/collections")
    soup = BeautifulSoup(response.text, 'html.parser')

    brand_links = []

    headings = soup.find_all('h2', {'class': 'col-span-full sm:col-span-2 text-lg sm:text-2xl'})

    for heading in headings:
        letter_container = heading.parent

        for link in letter_container.find_all('a'):
            brand_links.append(link['href'].replace("/collections/", ""))
    
    return brand_links


def get_item_links(): 
    print("Updating item links...")

    print("getting brand links...")
    brand_links = get_brand_links()

    item_links = []

    for brand in brand_links:
        print("getting item links for " + brand)
        response = requests.get('https://shop-us.doverstreetmarket.com/collections/' + brand)
        soup = BeautifulSoup(response.text, 'html.parser')

        # TODO if I really wanna grab everything I should use Selenium to scroll all the way down so that every item can load

        print("searching for strings with " + f"a[href^='/collections/{brand}/products']")
        items = soup.select(f'a[href^="/collections/{brand}/products"]')
        print(items.__len__())
        for item in items:
            item_name = item['href'].replace("/collections/aarahee/products/","")
            item_links.append((brand,item_name,'https://shop-us.doverstreetmarket.com/' + item["href"]))

    return item_links

    

