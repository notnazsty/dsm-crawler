import subprocess

# Call the setup.py file to install the project
subprocess.check_call(['python', 'setup.py', 'install'])


from bs4 import BeautifulSoup
import requests

response = requests.get("https://shop-us.doverstreetmarket.com/collections")

soup = BeautifulSoup(response.text, 'html.parser')


def write_array_to_text_file(fileName, array):
    with open(fileName, 'w') as f:
        for item in array:
            f.write(item + ',\n')


def get_brand_links():
    brand_links = []

    headings = soup.find_all('h2', {'class': 'col-span-full sm:col-span-2 text-lg sm:text-2xl'})

    for heading in headings:
        letter_container = heading.parent

        for link in letter_container.find_all('a'):
            brand_links.append('https://shop-us.doverstreetmarket.com/' + link['href'])
    
    return brand_links




write_array_to_text_file("links.txt",get_brand_links())