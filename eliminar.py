import urllib.request


def download_file_with_headers(url, save_path):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "Referer": "https://www.google.com/",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    try:
        request = urllib.request.Request(url, headers=headers or {})
        with urllib.request.urlopen(request) as response, open(save_path, 'wb') as file:
            file_size = response.getheader('Content-Length')
            file_size = int(file_size) if file_size else 0
            chunk_size = 8192
            downloaded = 0
            while chunk := response.read(chunk_size):
                file.write(chunk)
                downloaded += len(chunk)

    except Exception as e:
        print(f"Error: {e}")


url = "https://dictionary.cambridge.org/es/images/full/sun_noun_001_16945.jpg?version=6.0.39"
save_path = "delete_image.jpg"
download_file_with_headers(url, save_path)
