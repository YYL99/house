# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

'''
one     读写文本格式的数据
two     二进制数据格式
three   使用HTML和Web API
four    使用数据库
'''


def practice_one():
    obj = Series([4, 7, -5, 3])
    '''
    pandas解析函数
        read_csv        从文件、URL、文件型对象中加载带分隔符的数据,默认分隔符为逗号
        read_table      从文件、URL、文件型对象中加载带分隔符的数据,默认分隔符为制表符
        read_fwf        读取定宽列格式数据（没有分隔符）
        read_clipboard  读取剪贴板中的数据，可以看作read_table的剪贴板
    '''
    '''
    read_csv/read_table函数的参数：
        path            表示文件系统位置，URL，文件型对象的字符串
        sep,delimiter   用于对行中个字段进行拆分的字符序列或正则表达式
        header          用作列名的行号。默认0（第一行），若无则设置为None
        index_col       用作行索引的列编号或列名
        names           用于结果的列名列表
        skiprows        需要忽略的行数(从文件开始处算起)，或需要跳过的行号列表(从0开始)
        na_values       一组用于替换NA的值
        comment         用于将注释信息从行尾拆分出去的字符（一或多）
        parse_dates     将数据解析为日期，默认False；若为True，则尝试解析所有列。此外，还可以指定需要的一组列号或列名
        keep_data_col   如果连接多列解析日期，则保持参与连接的列。默认False
        converters      由列名/列名跟函数之间的映射关系组成的字典
        dayfirst        当解析有歧义的日期时，将其看做国际格式
        data_parser     用于解析日期的函数
        nrows           需要读取的行数
        iterator        返回一个TextParser以便逐块读取文件
        chunksize       文件块的大小（用于迭代）
        skip_footer     需要忽略的行数
        verbose         打印各种解析器输出信息
        encoding        用于unicode的文件编码格式
        squeeze         如果数据经解析后仅含一列，则返回Series
        thousands       千分位分隔符，如‘，’或‘。’
    '''

    # 逐块读取文本文件
    '''
    文件夹：ch06    文件名：ex6.csv
    '''
    # 在处理文件时若只想读取一小部分或对文件进行迭代
    pd.read_csv('ch06/ex6.csv')
    # 只想读取几行，通过nrows进行指定即可
    pd.read_csv('ch06/ex6.csv', nrows=5)
    # 逐块读取文件，需要设置chunksize（行数）, 返回TextParser对象
    chunker = pd.read_csv('ch06/ex6.csv', chunksize=10)
    tot = Series([])
    for piece in chunker:
        tot = tot.add(piece['message'].value_counts, fill_value=0)
        # 聚合到message列
    tot = tot.order(ascending=False)

    # 将数据写出到文本格式
    data = pd.read_csv('ch06/ex5csv')
    data.to_csv('ch06/out.csv')     # 将数据写入一个以逗号分隔的文件中
    data.to_csv(sys.stdout, sep='|')    # 分隔符为|
    data.to_csv(sys.stdout, na_rep='NULL')  # 缺失值表示为空字符串
    data.to_csv(sys.stdout, index=False, header=False)
    data.to_csv(sys.stdout, index=False, cols=['a', 'b', 'c'])

    # 手工处理分隔符格式
    import csv
    f = open('ch06/ex7.csv')
    reader = csv.reader(f)
    for line in reader:
        print(line)

    lines = list(csv.reader(open('ch06/ex7.csv')))
    header, values = lines[0], lines[1:]        # 分段
    data_dict = {h: v for h, v in zip(header, zip(*values))}
    # 定义csv.Dialect的一个子类，关于格式的
    class my_dialect(csv.Dialect):
        lineterminator = '\n'
        delimiter = ';'
        quotechar = '"'
    reader = csv.reader(f, dialect=my_dialect)
    reader = csv.reader(f, dialect='|')     # 不定义子类，直接提供
    '''
    csv.Dialect的属性及功能
        delimiter       用于分隔字段的单字符字符串，默认','
        lineterminator  用于写操作的行结束，默认'\r\n'
        quotechar       用于带有特殊字符的字段的引用符号，默认'"'
        quoting         引用约定。可选值包括csv.QUOTE_ALL(引用所有字段),
                        csv.QUOTE_MINIMAL(只引用带有如分隔符之类特殊字符的字段)，
                        csv.QUOTE_NONNUMERIC以及csv.QUOTE_NON(不引用)，默认QUOTE_MINIMAL
        skipinitialspace    忽略分隔符后面的空白符，默认False
        doublequote     处理字段内的引用符号。True,则双写
        escapechar      用于对分隔符进行转义的字符串，默认禁用
    '''
    with open('mydata.csv', 'w') as f:
        writer = csv.writer(f, dialect=my_dialect)
        writer.writerow(('one', 'two', 'three'))
        writer.writerow(('1', '2', '3'))
        writer.writerow(('4', '5', '6'))
        writer.writerow(('7', '8', '9'))

    # JSON数据
    obj = """
    {"name": "Wes",
     "places_lived": ["United States", "Spain", "Germany"],
     "pet": null,
     "siblings": [{"name": "Scott", "age": 25, "pet": "Zuko"},
                    {"name": "Katie", "age": 33, "pet": "Cisco"}]
    }
    """
    import json
    result = json.loads(obj)        # 将JSON对象转换为python格式
    json.dumps(result)              # 将python对象转换为JSON格式
    siblings = DataFrame(result['siblings'], columns=['name', 'age'])   # 将JSON对象转换为DataFrame

    # XML和HTML:Web信息收集
    from lxml.html import parse
    from urllib2 import urlopen     # 无法下载urllib2类
    parsed = parse(urlopen('http://finance.yahoo.com/q/op?s=AAPL+Options'))
    doc = parsed.getroot()
    links = doc.findall('.//a')     # 查询
    links[28].get('href')           # 获得url
    links[28].text_content()        # 获得文本
    urls = [links[28].get('href') for lnk in doc.findall('.//a')]   # 获得文档中全部URL

    tables = doc.findall('.//table')
    calls = tables[9]
    puts = tables[13]
    rows = calls.findall('.//tr')
    def _unpack(row, kind='td'):
        elts = row.findall('.//%s' % kind)
        return [val.text_content() for val in elts]
    _unpack(rows[1], kind='th')
    _unpack(rows[1], kind='td')
    from pandas.io.parsers import TextParser
    def parse_options_data(table):
        rows = table.findall('.//tr')
        header = _unpack(rows[0], kind='th')
        data = [_unpack(r) for r in rows[1:]]
        return TextParser(data, names=header).get_chunk()
    parse_options_data(calls)
    parse_options_data(puts)

    pass


def practice_two():
    frame = pd.read_csv('ch06/ex1.csv')     # 读
    frame.save('ch06/frame_pickle')         # 写     !!!出现错误，无法存储
    pd.load('ch06/frame_pickle')            # 读

    # 使用HDF5格式
    store = pd.HDFStore('mydata.h5')
    store['obj1'] = frame
    store['obj1_col'] = frame['a']

    # 读取Microsoft Excel文件   使用xlrd和openpyxl包
    xls_file = pd.ExcelFile('data.xls')     # 传入文件
    table = xls_file.parse('Sheet1')

    pass


def practice_three():
    # 使用requests包
    import requests
    url = 'http://search.twitter.com/search.json?q=python%20pandas'
    resp = requests.get(url)
    import json
    data = json.loads(resp.text)
    data.keys()     # 返回的JSON字符串，加载到python对象中
    tweet_fields = ['created_at', 'from_user', 'id', 'text']
    tweets = DataFrame(data['results'], columns=tweet_fields)   # 将results列表传给DataFrame
    tweets.ix[7]

    pass


def practice_four():
    import sqlite3      # 驱动器
    query = """
    CREATE TABLE test
    (a VARCHAR(20), b VARCHAR(20),
    c REAL,         d INTEGER
    );"""
    con = sqlite3.connect(':memory:')
    con.execute(query)
    con.commit()
    # 插入几行数据
    data = [('Atlanta', 'Georgia', 1.25, 6),
            ('Tallahassee', 'Florida', 2.6, 3),
            ('Sacramento', 'California', 1.7, 5)]
    stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"
    con.executemany(stmt, data)
    con.commit()
    cursor = con.execute('select * from test')
    rows =cursor.fetchall()
    import pandas.io.sql as sql
    sql.read_frame('select * from test', con)

    # 存储MongoDB中的数据     pymongo包
    import pymongo
    con = pymongo.Connection('localhost', port=27017)
    tweets = con.db.tweets
    import requests, json
    url = 'http://search.twitter.com/search.json?q=python%20pandas'
    data = json.loads(requests.get(url).text)
    for tweet in data['results']:
        tweets.save(tweet)
    cursor = tweets.find({'from_user': 'wesmckinn'})
    tweet_fields = ['created_at', 'from_suer', 'id', 'text']
    result = DataFrame(list(cursor), columns=tweet_fields)

    pass
