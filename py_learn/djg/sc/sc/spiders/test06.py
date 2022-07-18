import re
import urllib
import requests
import urllib.request
from lxml import etree

url = 'https://www.zhihu.com/question/264934683/answer/2408109124'
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
a = 167
for a1 in range(a):
    urla = 'https://pic.netbian.com/4kdongman/index_{}.html'.format(a1)
    print(urla)
pattern = re.compile('/')
response = urllib.request.urlopen(url)
data = response.read().decode("GBK")
print(data)
ta = etree.HTML(data)
#result = ta.xpath("/html/body//p/text()")
result = ta.xpath("//span[@class='RichText ztext CopyrightRichText-richText css-14bz7qe']/text()")
print(result)

for i in result:
    imgUrl = "https://pic.netbian.com" + i
    response = requests.get(imgUrl).content
    iList = pattern.split(i)
    store_url = "D:/a/img/" +iList[len(iList) - 1]
    with open(store_url, "wb") as f:
        f.write(response)
