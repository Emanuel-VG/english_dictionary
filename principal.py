from bs4 import BeautifulSoup
from urllib import request, error, parse
from extraction import Extraction
import io
import gzip
import re


def have_page(url, word, type_word):
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
    request_params = request.Request(url=(url+word), headers=missing_headers)
    try:
        html = request.urlopen(request_params)
    except error.URLError:
        print('Server Error')
        return
    except error.HTTPError:
        print('Page error')
        return
    except:
        print('Error')
        return
    word_url = (parse.urlparse(html.geturl()).path).replace(
        '/es/diccionario/ingles/', '')
    word_url = re.sub(r'[ _-]', '', word_url)
    print(word)
    if word_url != re.sub(r'[ _-]', '', word):
        return

    if html.headers.get('Content-Encoding') == 'gzip':
        # unzip response
        buffer = io.BytesIO(html.read())
        with gzip.GzipFile(fileobj=buffer) as f:
            decompressed_data = f.read()
        # decode to utl-8
            text_data = decompressed_data.decode('utf-8')
    else:
        text_data = html.read()
        text_data = text_data.decode('utf-8')

    page = BeautifulSoup(text_data, 'html.parser')
    contents = page.find_all('div', {'class': 'pr entry-body__el'})
    for content in contents:
        type = content.find('span', {'class': 'pos dpos'})
        if type == None:
            continue
        if type.get_text() == type_word:
            quote = Extraction(content)
            # quote.find_word()
            print(quote.pronunciation_uk())
            print(quote.pronunciation_us())
            print(quote.mp3_uk())
            print(quote.ogg_uk())
            print(quote.mp3_us())
            print(quote.ogg_us())
            print(quote.image_big())
            print(quote.image_small())
            print('ok')
            return
    if contents != []:
        pass


have_page('https://dictionary.cambridge.org/es/diccionario/ingles/',
          'cat', 'noun')
