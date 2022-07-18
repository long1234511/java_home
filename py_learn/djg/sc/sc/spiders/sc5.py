import re
import urllib
import requests
import urllib.request
from lxml import etree

url = 'https://www.zhihu.com/question/264934683/answer/2408109124'
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
pattern = re.compile('/')
response = urllib.request.urlopen(url)
print(response)
data = response.read().decode("UTF-8")
print(data)
ta = etree.HTML(data)
#result = ta.xpath("/html/body//p/text()")
result = ta.xpath("//span[@class='RichText ztext CopyrightRichText-richText css-14bz7qe']/text()")
print(result)
pattern1 = re.compile('[\u4e00-\u9fa5]+')
print(pattern1.findall(data))

a = ''.join(pattern1.findall(data))

with open("D:/ac.txt", "a") as f:
    f.write(a)
