# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

'''
one     合并数据集
'''


def practice_one():
    df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                     'data1': range(7)})
    df2 = DataFrame({'key': ['a', 'b', 'd'],
                     'data2': range(3)})
    pd.merge(df1, df2)      # 多对一的合并，未指定列连接时使用重叠列
    pd.merge(df1, df2, on='key')    # 指定列
    df3 = DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                     'data1': range(7)})
    df4 = DataFrame({'rkey': ['a', 'b', 'd'],
                     'data2': range(3)})
    pd.merge(df3, df4, left_on='lkey', right_on='rkey')     # 当列名不同时
    '''
    merge:
        默认做的是“inner”连接：键为交集；
        其他方式还有“left”，“right”，“outer”
        外连接求得是键的并集，结合了左连接和右连接的效果
    '''
    pd.merge(df1, df2, how='outer')
    df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                     'data1': range(6)})
    df2 = DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                     'data2': range(5)})
    pd.merge(df1, df2, on='key', how='left')    # 多对多合并
    pd.merge(df1, df2, how='inner')     # 多对多连接产生的是笛卡尔积
    left = DataFrame({'key1': ['foo', 'foo', 'bar'],
                      'key2': ['one', 'two', 'one'],
                      'lval': [1, 2, 3]})
    right = DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                       'key2': ['one', 'one', 'one', 'two'],
                       'rval': [4, 5, 6, 7]})
    pd.merge(left, right, on=['key1', 'key2'], how='outer')
    pd.merge(left, right, on='key1')
    pd.merge(left, right, on='key1', suffixes=('_left', '_right'))
    '''
    merge函数的参数
        left        参与合并的左侧DataFrame
        right       参与合并的右侧DataFrame
        how         'inner', 'outer', 'left', 'right'
        on          用于连接的列名
        left_on     左侧DataFrame中用作连接键的列
        right_on    右侧DataFrame中用作连接键的列
        left_index  将左侧的行索引用作其连接键
        right_index 类似于left_index
        sort        根据连接键对合并后的数据进行排序，默认True
        suffixes    字符串值元组，用于追加到重叠列名的末尾，默认True
        copy        设置为False
    '''

    # 索引上的合并
    left1 = DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
                       'value': range(6)})
    right1 = DataFrame({'group_val': [3.7, 7]}, index=['a', 'b'])
    pd.merge(left1, right1, left_on='key', right_index=True)
    pd.merge(left1, right1, left_on='key', right_index=True, how='outer')

    lefth = DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                       'key2': [2000, 2001, 2002, 2001, 2002],
                       'data': np.arange(5.)})
    righth = DataFrame(np.arange(12).reshape((6, 2)),
                       index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio','Ohio'],
                              [2001, 2000, 2000, 2000, 2001, 2002]],
                       columns=['event1', 'event2'])
    pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True)
    pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True, how='outer')
    left2 = DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=['a', 'c', 'e'],
                      columns=['Ohio', 'Nevada'])
    right2 = DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                       index=['b', 'c', 'd', 'e'], columns=['Missouri', 'Alabama'])
    pd.merge(left2, right2, how='outer', left_index=True, right_index=True)
    # join实例方法
    left2.join(right2, how='outer')
    left1.join(right1, on='key')
    another = DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],
                        index=['a', 'c', 'e', 'f'], columns=['New York', 'Oregon'])
    left2.join([right2, another])
    left2.join([right2, another], how='outer')

    # 轴向连接      concatenate连接，binding绑定，stacking堆叠
    arr = np.arange(12).reshape((3,4))
    np.concatenate([arr, arr], axis=1)
    s1 = Series([0, 1], index=['a', 'b'])
    s2 = Series([2, 3, 4], index=['c', 'd', 'e'])
    s3 = Series([5, 6], index=['f', '8'])
    pd.concat([s1, s2, s3])
    pd.concat([s1, s2, s3], axis=1)
    s4 = pd.concat([s1 * 5, s3])
    pd.concat([s1, s4], axis=1)
    pd.concat([s1, s4], axis=1, join='inner')
    pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']])
    result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])
    result.unstack()
    pd.concat([s1, s1, s3], axis=1, keys=['one', 'two', 'three'])
    df1 = DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'],
                    columns=['one', 'two'])
    df2 = DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'],
                    columns=['three', 'four'])
    pd.concat([df1, df2], axis=1, keys=['level1', 'level2'])

    pass
