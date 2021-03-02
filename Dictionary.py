# Word of the Day Program
# 2020 Adam McMullen
# Author: Adam McMullen <adammcmullen.com>
# URL: <https://github.com/adammcmullen/word-of-the-day/>


# This script scrapes Dictionary.com or uses the merrian webster api to get defintions to specific words

from urllib.request import urlopen

def get_definition(word,pythonAnywhere):

    # I can only use dictionary.com when running from my local machine.
    # PythonAnywhere doesn't have dictionary.com on its whitelist and will
    # return a 403 error see here: www.pythonanywhere.com/whitelist/
    # . When on PythonAnywhere servers I need to use the Merriam Webster api:
    # https://dictionaryapi.com/

    if pythonAnywhere:
        url = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/"+word+"?key=19df8f66-5b1f-44f1-a518-23f973a468f2"
        page = urlopen(url)

    else:
        url = "https://www.dictionary.com/browse/"+word
        page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    return html

#print(get_definition('pyrrhic',True)) # uncomment this line to test this module

