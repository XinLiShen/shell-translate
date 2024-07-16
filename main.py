import unicodedata
import sys
import json
import hashlib
import requests

app_id = '' # needed
key = '' # needed
salt = 'salt' # it can be anything
l_from = ''
l_to = ''
domain = 'it' # needed, the filed you want

def is_english(ch):
    return ch.isalpha() and unicodedata.name(ch).startswith('LATIN')

def is_chinese(ch):
    if ' radicals' in unicodedata.name(ch) or \
        unicodedata.east_asian_width(ch) in ['F', 'W']:
        return True
    return False

def tec_laungrage(q):
    for c in q:
        if is_chinese(c):
            return True
        elif is_english:
            return False
    return True

def getQ():
    ans = ''
    global l_from,l_to
    if len(sys.argv) < 2:
        print('wrong input')
        return 
    for arg in sys.argv:
        if arg == sys.argv[0]:
            continue
        ans += arg
    return ans

def s2md5(sign):
    md5_obj = hashlib.md5()
    md5_obj.update(sign.encode())
    return md5_obj.hexdigest()


def httpC(url):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        content = json.loads(content)
        dst = content["trans_result"][0]["dst"]
        return dst

def tran(q):
    if tec_laungrage(q):
        l_from = 'zh'
        l_to = 'en'
    else:
        l_from = 'en'
        l_to = 'zh'
    sign = app_id + q + salt + domain + key
    sign = s2md5(sign)
    url = 'http://api.fanyi.baidu.com/api/trans/vip/fieldtranslate' +   \
    '?q=' + q +                                                         \
    '&from=' + l_from +                                                 \
    '&to=' + l_to +                                                     \
    '&appid=' + app_id +                                                \
    '&salt=' + salt +                                                   \
    '&domain=' + domain +                                               \
    '&sign=' + sign
    res = httpC(url)
    print(res)
    return res

def main():
    q = getQ();
    if q != None:
        tran(q)

if __name__ == "__main__":
    main()
