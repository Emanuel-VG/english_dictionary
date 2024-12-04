import urllib.request


class Extraction:
    def __init__(self, content, dir):
        self.content = content
        self.dir = dir

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

    def find_word(self):
        try:
            word = self.content.find('span', {'class': 'hw dhw'}).get_text()
            return word
        except:
            return None

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
            return link_sound
        except:
            return None

    def ogg_uk(self):
        try:
            link_sound = self.content.find(
                'span', {'class': 'uk dpron-i'}).find('source', {'type': 'audio/ogg'})['src']
            return link_sound
        except:
            return None

    def mp3_us(self):
        try:
            link_sound = self.content.find(
                'span', {'class': 'us dpron-i'}).find('source', {'type': 'audio/mpeg'})['src']
            return link_sound
        except:
            return None

    def ogg_us(self):
        try:
            link_sound = self.content.find(
                'span', {'class': 'us dpron-i'}).find('source', {'type': 'audio/ogg'})['src']
            return link_sound
        except:
            return None

    def image_big(self):
        try:
            link_image = self.content.find(
                'div', {'class': 'dimg'}).find('amp-img')['src']
            image = link_image.replace('thumb', 'full')
            return image
        except:
            return None

    def image_small(self):
        try:
            link_image = self.content.find(
                'div', {'class': 'dimg'}).find('amp-img')['src']
            return link_image
        except:
            return None

    def list_data(self):
        data = []
        data.append(self.find_word())
        data.append(self.pronunciation_uk())
        data.append(self.pronunciation_us())
        data.append(self.mp3_uk())
        data.append(self.ogg_uk())
        data.append(self.mp3_us())
        data.append(self.ogg_us())
        data.append(self.image_big())
        data.append(self.image_small())
        return data
