# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

'''
one     读写文本格式的数据
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

    pass
