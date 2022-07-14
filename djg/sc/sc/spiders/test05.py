import re
import urllib
import requests
import urllib.request
from lxml import etree

url = 'https://www.cnblogs.com/leesf456/p/5344133.html'
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

data = requests.get(url, headers=headers).content.decode()
print(data)
ta = etree.HTML(data)
#result = ta.xpath("/html/body//p/text()")
result = ta.xpath("//div[@id='cnblogs_post_body']/p//text()")
print(result)