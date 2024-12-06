import urllib.request
import csv
import time


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
            time.sleep(0.5)
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
        word = self.content.find('span', {'class': 'hw dhw'})
        if word:
            self.word = word.get_text()

    def pronunciation_uk(self):
        aux = self.content.find('span', {'class': 'uk dpron-i'})
        if aux:
            pro_uk = aux.find('span', {'class': 'ipa dipa lpr-2 lpl-1'})
            return pro_uk.get_text() if pro_uk else None
        return None

    def pronunciation_us(self):
        aux = self.content.find('span', {'class': 'us dpron-i'})
        if aux:
            pro_us = aux.find('span', {'class': 'ipa dipa lpr-2 lpl-1'})
            return pro_us.get_text() if pro_us else None
        return None

    def mp3_uk(self):
        try:
            link_sound = self.content.find(
                'span', {'class': 'uk dpron-i'}).find('source', {'type': 'audio/mpeg'})['src']
            path = self.dir+'/mp3_uk/'+self.word+'.mp3'
            self.download_file(self.url_principal+link_sound, path)
            return 'mp3_uk/'+self.word+'.mp3'
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

    def examples(self):
        text = ''
        block_examples = self.content.find_all(
            'div', {'class': 'def-block ddef_block'})
        for block in block_examples:
            level_english = block.find('span', {'class': 'def-info ddef-info'})
            if level_english:
                text += level_english.get_text()
            meaning = block.find('div', {'class': 'def ddef_d db'})
            if meaning:
                text += ('-'+meaning.get_text())
            sentences = block.find_all('span', {'class': 'eg deg'})
            for sentence in sentences:
                text += ('*'+sentence.get_text())
            more_examples = block.find_all('li', {'class': 'eg dexamp hax'})
            for other_example in more_examples:
                text += ('*'+other_example.get_text())
            text += '|'
        return text[:-1] if text[-1] == '|' else text

    def create_data(self):
        data_word = [self.word, self.pronunciation_uk(), self.pronunciation_us(), self.mp3_uk(), self.ogg_uk(
        ), self.mp3_us(), self.ogg_us(), self.image_big(), self.image_small(), self.examples()]
        try:
            with open(self.dir+'/words.csv', mode='a', encoding='utf-8', newline='') as file_csv:
                writer = csv.writer(file_csv)
                writer.writerow(data_word)
        except Exception as e:
            print(f"Error to save data: {e}")
