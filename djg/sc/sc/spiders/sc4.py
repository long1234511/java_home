import requests
from bs4 import BeautifulSoup
from lxml import etree
import re
class BookUrl(object):
    def __init__(self):
        self.url = "https://b.faloo.com/995484_1.html"
        self.headers = {
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        self.response = []
    def send_request(self):
        count = 5
        for ai in range(count):
            print(ai)
            data = requests.get(self.url.format(ai), headers=self.headers).content.decode("GBK")
            #self.deal_data(data)
            self.deal_lxml_data(data)
    def deal_data(self, data):
        soup = BeautifulSoup(data, 'lxml')
        su = soup.find("div", class_="noveContent readline")
        if su:
            result = su.get_text()
            print(result)
            if result:
                with open("D:/a.txt", "a") as f:
                    f.write(result)
    def deal_lxml_data(self, data):
        soup = etree.HTML(data)
        result = soup.xpath('//div[@class="c_left"]//text()')
        # pattern = re.compile('[\u4e00-\u9fa5_0-9]+')
        #result = pattern.findall(data)
        print(result)
        if result:
            aa1 = "".join(result)
            with open("D:/a.txt", "a") as f:
                f.write(aa1)

BookUrl().send_request()


