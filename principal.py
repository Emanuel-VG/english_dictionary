import time
import search
import pathlib

principal_folder = 'data'
folder_name = 'topics'
category = 'noun'
file_name = 'weather_conditions.csv'
dir = 'data/noun/weather_conditions'


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
    dirs = [dir, dir+'/mp3_uk', dir+'/ogg_uk', dir+'/mp3_us',
            dir+'/ogg_us', dir+'/image_big', dir+'/image_small']
    for i in dirs:
        dir_create = pathlib.Path(i)
        dir_create.mkdir(parents=True, exist_ok=True)


def scraping_words(words_list, category, dir):
    time.sleep(1)
    for word in words_list:
        search.have_page(word, category, dir)


words = list_words_from_file(folder_name, category, file_name)
create_folders()
scraping_words(words, category, dir)
