#author: hanshiqiang365

import urllib.request
import json

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

if __name__ == '__main__':
    key = '334d13d8091e445cb04ba7f0bbb3f253'
    api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='

    while True:
        info = input('我: ')
        request = api + str(info.encode('utf-8'))
        response = getHtml(request)
        dic_json = json.loads(response)
        print('机器人: ' + dic_json['text'])
