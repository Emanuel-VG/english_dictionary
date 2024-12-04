from bs4 import BeautifulSoup
from urllib import request, error, parse
from extraction import Extraction
import io
import gzip
import re


def have_page(word, type_word, dir):
    url = 'https://dictionary.cambridge.org/es/diccionario/ingles/'
    missing_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip",
        "Accept-Language": "en-US,en;q=0.9",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "Referer": "https://www.google.com/",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    word = word.strip().replace(' ', '-').replace("'", '-').lower()
    request_params = request.Request(url=url+word, headers=missing_headers)
    try:
        html = request.urlopen(request_params)
    except error.URLError:
        print('Server Error')
        return
    except error.HTTPError:
        print('Page error')
        return
    except Exception as inst:
        print(inst)
        print('Other Error')
        return
    word_url_alt = (parse.urlparse(html.geturl()).path).replace(
        '/es/diccionario/ingles/', '')
    word_url = (re.sub(r'[^a-zA-Z]', '', word_url_alt)).lower()
    if word_url != re.sub(r'[^a-z]', '', word):
        print(word+": Not Found")
        return

    # unzip the file
    if html.headers.get('Content-Encoding') == 'gzip':
        buffer = io.BytesIO(html.read())
        with gzip.GzipFile(fileobj=buffer) as f:
            decompressed_data = f.read()
        # decode to utl-8
            text_data = decompressed_data.decode('utf-8')
    else:
        text_data = html.read()
        text_data = text_data.decode('utf-8')

    # find the block html
    page = BeautifulSoup(text_data, 'html.parser')
    contents = page.find_all('div', {'class': 'pr entry-body__el'})
    for content in contents:
        type_extracted = content.find('span', {'class': 'pos dpos'})
        if type_extracted == None:
            continue
        if type_word in type_extracted.get_text():
            quote = Extraction(content, dir, word_url_alt)
            quote.create_data()
            return
