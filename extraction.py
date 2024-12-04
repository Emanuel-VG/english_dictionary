import urllib.request
import csv


class Extraction:
    def __init__(self, content, dir, word):
        self.content = content
        self.dir = dir
        # dir = 'data/adjectives/animo'
        self.url_principal = 'https://dictionary.cambridge.org'
        self.word = word

    def download_file(self, url, save_path):
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

    def find_word(self):
        try:
            word = self.content.find('span', {'class': 'hw dhw'}).get_text()
            self.word = word
            return self.word
        except:
            return self.word

    def pronunciation_uk(self):
        try:
            pro_uk = self.content.find('span', {
                'class': 'uk dpron-i'}).find('span', {'class': 'ipa dipa lpr-2 lpl-1'}).get_text()
            return pro_uk

        except:
            return None

    def pronunciation_us(self):
        try:
            pro_us = self.content.find('span', {
                'class': 'us dpron-i'}).find('span', {'class': 'ipa dipa lpr-2 lpl-1'}).get_text()
            return pro_us
        except:
            return None

    def mp3_uk(self):
        try:
            link_sound = self.content.find(
                'span', {'class': 'uk dpron-i'}).find('source', {'type': 'audio/mpeg'})['src']
            path = self.dir+'/mp3_uk/'+self.word+'.mp3'
            self.download_file(self.url_principal+link_sound, path)
            return path
        except:
            return None

    def ogg_uk(self):
        try:
            link_sound = self.content.find(
                'span', {'class': 'uk dpron-i'}).find('source', {'type': 'audio/ogg'})['src']
            path = self.dir+'/ogg_uk/'+self.word+'.ogg'
            self.download_file(self.url_principal+link_sound, path)
            return 'ogg_uk/'+self.word+'.ogg'
        except:
            return None

    def mp3_us(self):
        try:
            link_sound = self.content.find(
                'span', {'class': 'us dpron-i'}).find('source', {'type': 'audio/mpeg'})['src']
            path = self.dir+'/mp3_us/'+self.word+'.mp3'
            self.download_file(self.url_principal+link_sound, path)
            return 'mp3_us/'+self.word+'.mp3'
        except:
            return None

    def ogg_us(self):
        try:
            link_sound = self.content.find(
                'span', {'class': 'us dpron-i'}).find('source', {'type': 'audio/ogg'})['src']
            path = self.dir+'/ogg_us/'+self.word+'.ogg'
            self.download_file(self.url_principal+link_sound, path)
            return 'ogg_us/'+self.word+'.ogg'
        except:
            return None

    def image_big(self):
        try:
            link_image = self.content.find(
                'div', {'class': 'dimg'}).find('amp-img')['src']
            image = link_image.replace('thumb', 'full')
            path = self.dir+'/image_big/'+self.word+'.jpg'
            self.download_file(self.url_principal+image, path)
            return 'image_big/'+self.word+'.jpg'
        except:
            return None

    def image_small(self):
        try:
            link_image = self.content.find(
                'div', {'class': 'dimg'}).find('amp-img')['src']
            path = self.dir+'/image_small/'+self.word+'.jpg'
            self.download_file(self.url_principal+link_image, path)
            return 'image_small/'+self.word+'.jpg'
        except:
            return None

    def create_data(self):
        try:
            # dir = 'data/adjectives/animo'
            with open(self.dir+'/words.csv', mode='a', encoding='utf-8', newline='') as file_csv:
                writer = csv.writer(file_csv)
                # ['sun', 'sʌn', 'sʌn', '/es/media/ingles/uk_pron/u/uks/uksom/uksomet012.mp3', '/es/media/ingles/uk_pron_ogg/u/uks/uksom/uksomet012.ogg', '/es/media/ingles/us_pron/s/son/son__/son.mp3', '/es/media/ingles/us_pron_ogg/s/son/son__/son.ogg', '/es/images/full/sun_noun_001_16945.jpg?version=6.0.39', '/es/images/thumb/sun_noun_001_16945.jpg?version=6.0.39']
                data_word = [self.find_word(), self.pronunciation_uk(), self.pronunciation_us(), self.mp3_uk(
                ), self.ogg_uk(), self.mp3_us(), self.ogg_us(), self.image_big(), self.image_small()]
                writer.writerow(data_word)
            print(data_word)
        except Exception as e:
            print(f"Error to save data: {e}")
