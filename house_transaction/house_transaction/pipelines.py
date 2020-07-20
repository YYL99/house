# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import MySQLdb

class HouseTransactionPipeline:
    def process_item(self, item, spider):
        return item

class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('house.json', 'w', encoding="utf-8")
    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item
    def spider_closed(self, spider):
        self.file.close()

class MysqlPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'root', '123456', 'house_transaction', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        for i in range(0, len(item["titles"][0])):
            insert_sql = """
                insert into house(titles, title_urls, looks, sizes, moneys)
                VALUE (%s, %s, %s, %s, %s)
            """
            self.cursor.execute(insert_sql, (item["titles"][0][i], item["title_urls"][0][i], item["looks"][0][i],
                                         item["sizes"][0][i],item["moneys"][0][i]))
            self.conn.commit()