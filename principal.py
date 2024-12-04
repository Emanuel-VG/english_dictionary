import csv
import time
import search
import pathlib

principal_folder = 'data/'
folder_name = 'topics'
category = 'noun'
file_name = 'weather conditions.csv'


def send_attributes():
    pass


def list_words_from_file(folder_name, category, file_name,):
    words = []
    url_path = folder_name + '/'+category+'/'+file_name
    with open(url_path, mode='r', encoding='utf-8') as file:
        for line in file:
            dato = line.strip()
            if dato:
                words.append(dato)
                # print(dato)
    return words


def create_folders():
    p = pathlib.Path((principal_folder+file_name).replace('.csv'))
    p.mkdir(parents=True, exist_ok=True)


def scraping_words(words_list, category):
    time.sleep(1)
    for word in words_list:
        search.have_page(word, category)


words = list_words_from_file(folder_name, category, file_name)
scraping_words(words, category)
