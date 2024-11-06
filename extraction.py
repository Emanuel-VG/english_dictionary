import json
import re


class Extraction:
    def __init__(self, content):
        self.content = content
        # print(self.content.get_text().replace('\n', ' ').strip())
        # print(self.content.find('div', {'class': 'dimg'}).prettify())

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
