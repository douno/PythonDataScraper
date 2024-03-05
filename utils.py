import requests, json, re, math, time, glob
from bs4 import BeautifulSoup

import socket
import requests
import json
import time
import glob
import pandas as pd

def get_the_soup(api_url):
    data = requests.get(api_url)
    soup = BeautifulSoup(data.content, 'html.parser')
    return soup

def write_to_doc(file_name, data):
    with open(file_name, 'w') as outfile:
        json.dump(data, outfile)

def download_remote_image(image_url, img_name):
    response = requests.get(image_url)
    file = open(img_name, "wb")
    file.write(response.content)
    file.close()

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
