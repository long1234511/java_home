# Define your item pipelines here
# 数据处理层
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Scrapy01Pipeline:
    def process_item(self, item, spider):
        print(1111)
        #数据出来层
        print(item)
        return item
