import re
import requests
from lxml import etree

url = 'http://news.baidu.com/'
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

# response.text 不太准确 转码 是靠推测
data = requests.get(url, headers=headers).content.decode()

# 正则解析 数据
#  每个新闻的titile, url

# <a href="http://news.cnr.cn/native/gd/20181028/t20181028_524397644.shtml" target="_blank" mon="r=1">习近平给民营经济再吃定心丸,民企当体会怎样深意</a>

pattern = re.compile('<a href="(.*?)" target="_blank" mon="(.*?)">(.*?)</a>')
# pattern = re.compile('<a (.*?)</a>',re.S)
pattern1 = re.compile('[\u4e00-\u9fa5]+')

print(pattern1.findall(data))
result = pattern.findall(data)

print(result)



# 1.转解析类型
xpath_data = etree.HTML(data)


# xpath 语法 1. 节点 /
#            2. 跨节点: //
#            3. 精确的标签: //a[@属性="属性值"]
#            4. 标签包裹的内容 text()
#            5. 属性:@href
#              xpath--s数据类型---list
# 2调用 xpath的方法
#result = xpath_data.xpath('/html/head/title//text()')
#result = xpath_data.xpath('//a/text()')
#result = xpath_data.xpath('//a[@mon="ct=1&a=2&c=top&pn=18"]/text()')
#result = xpath_data.xpath('//a[@mon="ct=1&a=2&c=top&pn=18"]/@href')
#result = xpath_data.xpath('//li/a/text()')

print(result)

# with open('02news.html', 'w') as f:
#     f.write(data)

# with open('02news.html', 'w') as f:
#     f.write(data)
html = """
    <html>
    <body>
    <ul>
     <li>1
         <a href="">子</a>
     </li>
     <li>2
        <a href="">子1</a>
     </li>
     <li>3
        <a href="">子2</a>
     </li>
     <li>4
         <a href="">子3</a>
     </li>
     <li>5
        <a href="">子4</a>
     </li>
     <b>11</b>
 </ul>
 </body>
 </html>
"""
# 1.转类型
x_data = etree.HTML(html)

# 2.xpath 下标 是从 1开始; 只能取 平级关系的标签
#result = x_data.xpath('//li[5]/text()')


result1 = x_data.xpath('/html/body/ul/li/a/text()')
result1 = x_data.xpath('/html/body/ul/b/text()')



print(result1)