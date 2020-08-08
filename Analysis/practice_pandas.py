# -*- coding: utf-8 -*-

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

'''
one     pandas的数据结构
two     基本功能
'''


def practice_one():
    obj = Series([4, 7, -5, 3])     # 由一组数据以及索引组成
    obj.values      # array([ 4,  7, -5,  3], dtype=int64)
    obj.index       # RangeIndex(start=0, stop=4, step=1)

    obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])    # 固定索引
    obj2[obj2 > 0]      # 大于0
    obj2 * 2            # 值乘以2
    np.exp(obj2)        # 各元素的指数
    'b' in obj2         # 返回True
    'e' in obj2         # 返回False

    sdata = {'o': 35, 't': 71, 'r': 16, 'u': 50}    # 放入字典中
    obj3 = Series(sdata)        # 通过字典进行创建
    states = ['C', 'o', 'r', 't']
    obj4 = Series(sdata, index=states)      # 进行对应显示
    pd.isnull(obj4)     # 检测缺失数据，缺失返回True
    pd.notnull(obj4)    # 检测缺失数据，缺失返回False
    obj4.isnull()       # 用于Series
    obj3 + obj4         # 自动对齐不同索引额数据
    obj4.name = 'population'    # 本身自带name属性
    obj4.index.name = 'state'

    obj.index = ['b', 's', 'j', 'r']    # 通过赋值方式改变默认索引

    data = {'state': ['o', 'o', 'o', 'n', 'n'],
            'year': [2000, 2001, 2002, 2001, 2002],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
    frame = DataFrame(data)         # 生成二维结构
    DataFrame(data, columns=['year', 'state', 'pop'])       # 指定列的排列顺序
    frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                       index=['one', 'two', 'three', 'four', 'five'])       # 若找不到产生NA值
    frame2.columns      # 返回排列顺序
    frame2['state']     # 返回state的值
    frame2.year         # 返回year的值
    frame2.ix['three']  # 返回three行
    frame2['debt'] = 16.5   # 添加值
    frame2['debt'] = np.arange(5.)      # 修改值

    val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
    frame2['debt'] = val        # 根据索引更改值

    frame2['eastern'] = frame2.state == 'o'     # 添加列，以state的o为True
    del frame2['eastern']       # 删除列

    pop = {'N': {2001: 2.4, 2002: 2.9},
           'O': {2000: 1.5, 2001: 1.7, 2002: 3.6}}      # 嵌套字典
    frame3 = DataFrame(pop)
    frame3.T        # 转置
    frame3.index.name = 'year'; frame3.columns.name = 'state'
    frame3.values

    '''
    Index的方法和属性
        append      连接另一个index对象，产生一个新的index
        diff        计算差集，得到一个index
        intersection    计算交集
        union       计算并集
        isin        计算一个指示各值是否都包含在参数集合中的布尔型数组
        delete      删除索引i处的元素，得到新的index
        drop        删除传入的值，得到index
        insert      将元素插入索引i处，得到新的index
        is_monotonic    当各元素均大于等于前一个元素时，返回True
        is_unique       当index没有重复时，返回True
        unique      计算index中唯一值的数组
    '''

    pass


def practice_two():
    # 重新索引      reindex
    obj = Series(['b', 'p', 'y'], index=[0, 2, 4])
    obj.reindex(range(6), method='ffill')
    '''
    ffill   前向填充值
    bfill   后向填充值
    pad     前向搬运值
    backfill    后向搬运值
    '''

    frame = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],
                      columns=['Ohio', 'Texas', 'California'])
    # 3行3列的数组，行索引为index，列索引为columns
    frame2 = frame.reindex(['a', 'b', 'c', 'd'])    # 添加索引为b这一行
    states = ['Texas', 'Utah', 'California']
    frame.reindex(columns=states)       # 使用columns可重新索引列
    '''
    reindex函数的参数
        index       用作索引的新序列
        method      插值方式
        fill_value  重新索引的过程中，需要引入缺失值时使用的代替值
        limit       前向或后向填充时的最大填充量
        level       在Multilndex的指定级别上匹配简单索引，否则取其子集
        copy        默认True，无论如何都复制；若为False，则新旧相等不复制
    '''

    # 丢弃指定轴上的项
    obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
    obj.drop('c')       # 删除c行
    obj.drop(['d', 'c'])    # 删除d,c行
    data = DataFrame(np.arange(16).reshape((4, 4)),
                     index=['o', 'c', 'u', 'n'],
                     columns=['one', 'two', 'three', 'four'])
    data.drop(['two', 'four'], axis=1)      # 删除列，two，four

    # 索引，选取，过滤

    pass
