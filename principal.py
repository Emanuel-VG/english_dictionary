import time
import search
import pathlib
principal_folder = 'data'
folder_name = 'topics'
category = ''                       # varia
file_name = 'weather_conditions.csv'    # varia
# dir = 'data/noun/weather_conditions'    # varia


def search_files():

    base_path = pathlib.Path(folder_name)
    folders = (entry for entry in base_path.iterdir())
    for folder_category in folders:
        global category
        category = folder_category.name
        aux = pathlib.Path(folder_category.__str__())
        folders_and_files = (entry for entry in aux.iterdir())
        for folder_or_file in folders_and_files:
            if folder_or_file.is_file():
                dir = 'data/'+category+'/' + folder_or_file.stem
                words = list_words_from_file(folder_or_file.__str__())
                create_folders(dir)
                scraping_words(words, category, dir)
            if folder_or_file.is_dir():
                aux2 = pathlib.Path(folder_or_file.__str__())
                files = (entry for entry in aux2.iterdir())
                for file in files:
                    if file.is_file():
                        dir = 'data/'+category+'/'+folder_or_file.name+'/'+file.stem
                        words = list_words_from_file(file.__str__())
                        create_folders(dir)
                        scraping_words(words, category, dir)


def list_words_from_file(file_dir):
    words = []
    with open(file_dir, mode='r', encoding='utf-8') as file:
        words = [line.strip().replace(' ', '-').replace("'", '-').lower()
                 for line in file if line.strip()]
    return words


def create_folders(dir):
    dirs = ['', '/mp3_uk', '/ogg_uk', '/mp3_us',
            '/ogg_us', '/image_big', '/image_small']
    for i in dirs:
        dir_create = pathlib.Path(dir+i)
        dir_create.mkdir(parents=True, exist_ok=True)


def scraping_words(words_list, category, dir):
    print('-----------------------------' +
          dir+'-------------------------------')
    for word in words_list:
        time.sleep(1)
        search.have_page(word, category, dir)


# words = list_words_from_file(folder_name, category, file_name)
# create_folders()
# scraping_words(words, category, dir)
search_files()
