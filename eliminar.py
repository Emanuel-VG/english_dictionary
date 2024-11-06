# import the required libraries
from urllib import request, error
from bs4 import BeautifulSoup
import io
import gzip
# define new request headers
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

# catch HTTP errors
try:

    # create a request param and add request headers
    request_params = request.Request(
        url="https://dictionary.cambridge.org/es/diccionario/ingles-espanol/cat",
        headers=missing_headers
    )

    # send the request with the parameters and obtain a response object
    response = request.urlopen(request_params)
    if response.headers.get('Content-Encoding') == 'gzip':
        # Descomprimir la respuesta
        buffer = io.BytesIO(response.read())
        with gzip.GzipFile(fileobj=buffer) as f:
            decompressed_data = f.read()
        # Decodificar a UTF-8 si es texto
            text_data = decompressed_data.decode('utf-8')
    else:
        text_data = response.read()
        text_data = text_data.decode('utf-8')
    soup = BeautifulSoup(text_data, 'html.parser')
    textos = soup.find_all('span', {'class', 'ipa dipa'})
    for text in textos:
        print(text.get_text())


except error.HTTPError as e:
    print(e)
