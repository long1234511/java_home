import re
import urllib
import requests
import urllib.request
from lxml import etree
import random
import string

def get_url(i):
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8745119118403747183&ipn=rj&ct=201326592&is=&fp=result&fr=ala&word=%E5%A5%BD%E7%9C%8B%E7%9A%84%E6%A1%8C%E9%9D%A2%E8%83%8C%E6%99%AF&queryWord=%E5%A5%BD%E7%9C%8B%E7%9A%84%E6%A1%8C%E9%9D%A2%E8%83%8C%E6%99%AF&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&expermode=&nojc=&isAsync=&pn='+str(i)+'&rn=30&gsm=1e&1657783070696='
    #url = 'https://image.baidu.com/search/acjson?tn=resulttagjson&logid=8553745808182457924&ie=utf-8&fr=ala&word=%E5%A5%BD%E7%9C%8B%E7%9A%84%E8%83%8C%E6%99%AF%E5%9B%BE%E5%8F%A4%E9%A3%8E&ipn=r&fm=index&pos=history&queryWord=%E5%A5%BD%E7%9C%8B%E7%9A%84%E8%83%8C%E6%99%AF%E5%9B%BE%E5%8F%A4%E9%A3%8E&cl=2&lm=-1&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&expermode=&nojc=&isAsync=true&pn='+str(i)+'&rn=30&itg=1&gsm=1e&1657780084778=';
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content.decode()
    #print(data)
    results = re.findall('.*?"hoverURL":"(.*?)",.*?', data)
    return results

def download_url(results,j):
    i = j
    for item in results:
        response = requests.get(item).content
        i = i + 1
        store_url = "D:\\a\\img\\back1\\" + str(i) +".jpg"
        with open(store_url, "wb") as f:
            f.write(response)

if __name__ == '__main__':
    i = 0
    for a1 in range(15):
        i = i + 30
        try:
            results = get_url(i)
            print(len(results))
            if len(results) > 0:
                print(results)
                download_url(results,i)
        except BaseException as f:
            print(f)

