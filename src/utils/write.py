import json
import csv
import os

def write_array_to_text_file(fileName, array):
    with open(fileName, 'w') as f:
        for item in array:
            f.write(item + ',\n')


def write_item_links_to_csv(data):
    output_dir = os.path.dirname("out/item_links.csv")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open("out/item_links.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['BrandName', 'ItemName', 'Link']) 
        for row in data:
            writer.writerow(row)


def save_jsonld_to_file(jsonld_string, filename):
    data = json.loads(jsonld_string)
    with open(filename, 'w') as f:
        json.dump(data, f)