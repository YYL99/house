# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import MySQLdb
from twisted.enterprise import adbapi
import MySQLdb.cursors

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
        # 同步的机制写入MySQL
        for i in range(0, len(item["titles"][0])):
            insert_sql = """
                insert into house(titles, title_urls, looks, sizes, moneys)
                VALUE (%s, %s, %s, %s, %s)
            """
            self.cursor.execute(insert_sql, (item["titles"][0][i], item["title_urls"][0][i], item["looks"][0][i],
                                         item["sizes"][0][i],item["moneys"][0][i]))
            self.conn.commit()


class MysqlTwistedPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host = settings["MYSQL_HOST"],
            db = settings["MYSQL_DBNAME"],
            user = settings["MYSQL_USER"],
            passwd = settings["MYSQL_PASSWORD"],
            charset = 'utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode = True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)

        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error)

    def handle_error(self, failure, item, spider):
        # 处理异步插入的异常
        print(failure)

    def do_insert(self, cursor, item):
        # 执行具体插入
        for i in range(0, len(item["titles"][0])):
            insert_sql = """
                insert into house(titles, title_urls, looks, sizes, moneys)
                VALUE (%s, %s, %s, %s, %s)
            """
            cursor.execute(insert_sql, (item["titles"][0][i], item["title_urls"][0][i], item["looks"][0][i],
                                         item["sizes"][0][i],item["moneys"][0][i]))
