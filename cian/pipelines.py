# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class CianPipeline:
    """Cian.ru parser pipeline."""

    def __init__(self):
        """Consturctor."""
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.cian

    def process_item(self, item, spider):
        """Process item."""
        collection = self.mongo_base[spider.name]
        collection.update_one(item, {'$setOnInsert': item}, upsert=True)

        return item
