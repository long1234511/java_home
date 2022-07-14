import string
import urllib
import urllib.parse
import urllib.request


def load_data():
    url = "http://www.baidu.com/"
    # get的请求
    # http请求
    # response:http相应的对象
    response = urllib.request.urlopen(url)
    print(response)
    # 读取内容 bytes类型
    data = response.read()
    print(data)
    # 将文件获取的内容转换成字符串
    str_data = data.decode("utf-8")
    print(str_data)
    # 将数据写入文件
    with open("D://a.html", "w", encoding="utf-8")as f:
        f.write(str_data)
    # 将字符串类型转换成bytes
    str_name = "baidu"
    bytes_name = str_name.encode("utf-8")
    print(bytes_name)

    # python爬取的类型:str bytes
    # 如果爬取回来的是bytes类型:但是你写入的时候需要字符串 decode("utf-8")
    # 如果爬取过来的是str类型:但你要写入的是bytes类型 encode(""utf-8")





def load_data02():
    url = "http://www.baidu.com?"
    param = {
        "wd": "中午",
        "key": "zs",
        "value": "san"
    }
    str_params = urllib.parse.urlencode(param)
    print("AAAAAA===========" + str_params)
    final_url = url + str_params

    # 将带有中文的url 转译成计算机可以识别的url
    end_url = urllib.parse.quote(final_url, safe=string.printable)
    print("BBBBBB " + end_url)
    response = urllib.request.urlopen(end_url)

    data = response.read().decode("utf-8")
    print(data)


def load_data03():
    url = "https://www.baidu.com"
    header = {
        # 浏览器的版本
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        # "haha":"hehe"
    }

    # 创建请求对象
    request = urllib.request.Request(url)
    # 动态的去添加head的信息
    request.add_header("User-Agent",
                       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
    # 请求网络数据(不在此处增加请求头信息因为此方法系统没有提供参数)
    response = urllib.request.urlopen(request)
    print(response)
    data = response.read().decode("utf-8")

    # 获取到完整的url
    final_url = request.get_full_url()
    print(final_url)

    # 响应头
    # print(response.headers)
    # 获取请求头的信息(所有的头的信息)
    # request_headers = request.headers
    # print(request_headers)
    # (2)第二种方式打印headers的信息
    # 注意点:首字母需要大写,其他字母都小写
    request_headers = request.get_header("User-agent")
    # print(request_headers)
    with open("D:/b.txt", "w")as f:
        f.write(data)


def load_data04():
    url = "https://www.baidu.com"
    response = urllib.request.urlopen(url)
    request = urllib.request.Request(url)
    request_head = request.headers

    print(request_head)


if __name__ == '__main__':
    load_data04()
