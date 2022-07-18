from selenium import webdriver
import re
import requests


filename = 'D://image'


def get_url():
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8553745808182457924&ipn=rj&ct=201326592&is=&fp=result&fr=ala&word=%E5%A5%BD%E7%9C%8B%E7%9A%84%E8%83%8C%E6%99%AF%E5%9B%BE&queryWord=%E5%A5%BD%E7%9C%8B%E7%9A%84%E8%83%8C%E6%99%AF%E5%9B%BE&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&expermode=&nojc=&isAsync=&pn=120&rn=30&gsm=78&1657779065760='
    brower = webdriver.Chrome()
    brower.get(url)
    items = brower.find_elements_by_tag_name('strong')
    result1 = []
    for item in items:
        text = item.text
        results = re.findall('.*?"hoverURL":"(.*?)",.*?', text)
        for result in results:
            if result not in result1:
                result1.append(result)
    brower.close()
    return result1


def save_img(results, j):
    for result in results:
        try:
            response = requests.get(result)
            path = filename + '/' + str(j) + '.jpg'
            j += 1
            with open(path, 'wb') as f:
                f.write(response.content)
                f.close()

        except requests.exceptions.MissingSchema:
            pass


if __name__ == '__main__':
    results = get_url()
    print(results)
