# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .database import dbClient
import pymongo

class SpidersnestPipeline:
    def __init__(self):
        client = dbClient
        db = client.spidersNestData
        self.boletimEconomicoCollection = db['boletim_economico_data_tb']
        self.infoMoneyCollection = db['info_money_data_tb']
        self.uolEconomiaCollection = db['uol_economia_data_tb']
    
    def process_item(self, item, spider):
        if(spider.name == "boletimEconomico"):
            self.boletimEconomicoCollection.insert(dict(item))
        elif(spider.name == "uolEconomia"):
            self.uolEconomiaCollection.insert(dict(item))
        elif(spider.name == "infoMoney"):
            self.infoMoneyCollection.insert(dict(item))
        return item
