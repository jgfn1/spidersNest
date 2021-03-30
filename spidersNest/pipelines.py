# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo



class SpidersnestPipeline:
    def __init__(self):
        client = pymongo.MongoClient("mongodb+srv://spiderdb:spiderdb1@cluster0.i3n8n.mongodb.net/spidersNestData?retryWrites=true&w=majority")
        db = client.spidersNestData
        self.collection = db['spiders_data_tb']
    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
