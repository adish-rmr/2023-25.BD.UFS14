import pickle
import datetime
import os
import re
import requests
from pypdf import PdfReader
from bs4 import BeautifulSoup
from pymongo import MongoClient

def open_data():
    try:
        with open("./data/ingredient.pkl", "rb") as pickle_file:
            ingredient = pickle.load(pickle_file)
    except Exception as e:
        with open("./data/cir_rep.html", encoding="utf8") as cir:
            soup = BeautifulSoup(cir, 'html.parser')

        table = soup.find('table', class_='table')

        for row in table.find_all('tr')[1:]:  # il primo elemento è "ingrediente as used.." e va saltato
            link = row.find('a')
            name = link.text
            url = link['href']
            ingredient[name] = url
    return ingredient