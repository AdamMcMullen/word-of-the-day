# Word of the Day Program
# 2020 Adam McMullen
# Author: Adam McMullen <adammcmullen.com>
# URL: <https://github.com/adammcmullen/word-of-the-day/>


# This script scrapes Dictionary.com to get defintions to specific words

from urllib.request import urlopen


def get_definition(word):
    
    url = "https://www.dictionary.com/browse/"+word
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    definition=html
    

    return definition

#print(get_definition('pyrrhic'))
