from bs4 import BeautifulSoup

import requests
import json
import pandas as pd
import glob


def aggregate_classification(data):
    urls = []
    for link in data:
        if link['url'] not in urls:
            urls.append(link['url'])

    all_links = []
    for url in urls:
        obj = {}
        obj['url'] = url
        obj['categories'] = []
        for d in data:
            if d['url'] == url:
                obj['categories'].append(d['category'])
        all_links.append(obj)

    return all_links



def check_tag_has_attribute(tag, attr):
    return tag.has_attr(attr)


def clean_text(txt):
    return txt.replace('\n', '').strip()

# reas csv file and add to data
def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
    # read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into a python dictionary
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python json array to json string and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
        

def get_the_soup(api_url):
    data = requests.get(api_url)
    soup = BeautifulSoup(data.content, 'html.parser')
    return soup

def download_remote_image(image_url, img_name):
    response = requests.get(image_url)
    file = open(img_name, "wb")
    file.write(response.content)
    file.close()


def get_keys(data):
    keys_list = []
    for d in data:
        for k in d.keys():
            if k not in keys_list:
                keys_list.append(k)
    return keys_list


def get_soup_text(item):
    return item.select(item)[0].get_text()

def get_tag_id(tag):
    return tag.get("id")
    

def get_url_from_list_of_links(arr):
    new_arr = []
    for a in arr:
        if a['href'] not in new_arr:
            new_arr.append(a['href'])
    return new_arr
    

def json_to_csv(input,output):
    df = pd.read_json(input)
    df.to_csv(output)
    print('Conversion completed!')


def list_links(my_arr):
    for x in my_arr:
        print(x)


def open_html_file(filename):
    with open(filename) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    return soup
    

def open_multiple_files(path):
    links = []
    for file in glob.iglob(r'{}'.format(path)):
        f = open(file,)
        data = json.load(f)
        for i in data:
            links.append(i)
        f.close()
    return links

def read_json_file(filename):
    f = open(filename,)
    return json.load(f)


def write_to_html(filename, content):
    file = open(filename,"w")
    file.write(content)
    file.close()


def write_to_json(file_name, data):
    with open(file_name, "w") as outfile:
        json.dump(data, outfile)
