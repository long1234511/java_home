from scrapy import cmdline
import os
# cmdline.execute("scrapy crawl tag ".split())  # 第一种写法
# cmdline.execute(["scrapy", "crawl", "tag"])	# 第二种写法
os.system('scrapy crawl tag novel')