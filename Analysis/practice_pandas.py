# -*- coding: utf-8 -*-

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

'''
one     pandas的数据结构
two     基本功能
three   汇总和计算描述统计
four    处理缺失数据
five    层次化索引
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
    obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
    obj['b']        # 等价于obj[1]
    obj[2:4]
    obj[['b', 'a', 'd']]
    obj[[1, 3]]
    obj[obj < 2]
    obj['b':'c']
    obj['b':'c'] = 5        # 修改值
    '''
    DataFrame的索引选项
        obj[val]          选取单列或一组列
        obj.ix[val]       单行或一组行
        obj.ix[val1, val2]  同时选取行和列
        reindex方法       将一个或多个轴匹配到新索引
        xs方法            根据标签选取单行或单列，返回Series
        icol,irow方法     根据整数位置选取单列或单行，返回Series
        get_value,set_value方法   根据行标签和列标签选取单个值
    '''

    # 算术运算和数据对齐
    s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
    s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'd', 'e', 'f', 'g'])
    s1 + s2     # 在不重叠的索引处引入NA值
    # 同样会发生在DataFrame上
    s1.add(s2, fill_value=0)        # 不会出现NA值，单纯加
    s1.reindex(columns=s2.columns, fill_value=0)        # 指定值
    '''
    add     +
    sub     -
    div     /
    mul     *
    '''

    frame = DataFrame(np.arange(12.).reshape((3, 4)),
                      columns=list('bde'),
                      index=['U', 'O', 'T', 'R'])
    series = frame.ix[0]
    frame - series
    series2 = Series(range(3), index=['b', 'e', 'f'])
    frame + series2     # 会出现NA值
    series3 = frame['d']
    frame.sub(series3, axis=0)

    # 函数应用与映射
    frame = DataFrame(np.random.randn(3, 4),
                      columns=list('bde'),
                      index=['U', 'O', 'T', 'R'])
    np.abs(frame)       # 绝对值
    f = lambda x: x.max() - x.min()
    frame.apply(f)
    frame.apply(f, axis=1)
    format = lambda x: '%.2f' %x
    frame.applymap(format)
    frame['e'].map(format)

    # 排序和排名
    '''
    .sort_index()       按字典顺序排序     行
    .sort_index(axis=1)         列
    .sort_index(ascending=False)        降序，默认升
    .order()            对Series
    .sort_index(by='*')         针对*列
    .rank(ascending=False,method='first',axis=1)
    # 'average' 默认，平均   'min' 最小    'max' 最大    'first' 按值在原始出现顺序分配排名
    '''

    # 带有重复值的轴索引
    obj = Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
    obj.index.is_unique     # 值是否唯一

    pass


def practice_three():
    df = DataFrame([[1.4, np.nan], [7.1, -4.5],
                    [np.nan, np.nan], [0.75, -1.3]],
                   index=['a', 'b', 'c', 'd'],
                   columns=['one', 'two'])
    df.sum()        # 列求和
    df.sum(axis=1)  # 行求和
    df.mean(axis=1, skipna=False)
    '''
    axis        0行，1列
    skipna      排除缺失值
    level       分组约简
    '''
    df.idxmax()         # .idxmax()，.idxmin()间接统计，达到最小值或最大值的索引
    df.cumsum()         # 累计型
    df.describe()       # 用于一次性产生多个汇总统计
    '''
    描述和汇总统计
        count           非NA值得数量
        describe        针对Series或各DataFrame列计算汇总统计
        min,max         计算最大值最小值
        argmin,argmax   计算最大值最小值的索引位置
        idxmin,idxmax   计算最大值最小值的索引值
        quantile        计算样本的分位数（0到1）
        sum             值的和
        mean            值的平均数
        median          值的算术中位数（50%分位数）
        mad             根据平均值计算平均绝对离差
        var             样本值的方差
        std             样本值的标准差
        skew            样本值的偏度（三阶矩）
        kurt            样本值的峰度（四阶矩）
        cumsum          样本值的累计和
        cummin,cummax   样本值的累计最大值和累计最小值
        cumprod         样本值的累计积
        diff            计算一阶差分（对时间序列很有用）
        pct_change      计算百分数变化
    '''

    # 相关系数与协方差
    '''
    .tail()
    .corr()
    .cov()
    .corrwith()
    '''

    # 唯一值、值计数以及成员资格
    obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b','c', 'c'])
    obj.unique()        # 得到唯一值
    obj.value_counts()      # 计算各值出现的频率
    pd.value_counts(obj.values, sort=False)     # 同上，可用于数组或序列
    obj.isin(['b', 'c'])        # 判断矢量化集合的成员资格

    pass


def practice_four():
    string_data = Series(['aa', 'ar', np.nan, 'av'])
    string_data.isnull      # 判断是否为NA
    string_data[0] = None
    string_data.isnull()    # 内置的None值也会当作NA处理
    '''
    NA处理方法
        dropna      根据各标签的值中是否存在缺失数据对轴标签进行过滤
        fillna      用指定值或插值方法（ffill或bfill）填充缺失数据
        isnull      返回一个布尔值的对象，表明哪些值是缺失值NA
        notnull     isnull的否定式
    '''

    # 滤除缺失数据
    from numpy import nan as NA
    data = Series([1, NA, 3.5, NA, 7])
    data.dropna()       # 返回一个仅含非空数据和索引值的Series
    data[data.notnull()]    # 同上
    data = DataFrame([[1., 6.5, 3.], [1., NA, NA],
                      [NA, NA, NA], [NA, 6.5, 3.]])
    data.dropna()       # 默认丢弃任何含有缺失值的行
    data.dropna(how='all')  # 只丢弃全为NA的那些行
    data.dropna(axis=1, how='all')  # 只丢弃全为NA的那些列
    df = DataFrame(np.random.randn(7, 3))
    df.ix[:4, 1] = NA
    df.ix[:2, 2] = NA
    df.dropna(thresh=3)

    # 填充缺失数据
    df.fillna(0)        # 填充为0
    df.fillna({1: 0.5, 3: -1})      # 可以实现对不同的列填充不同的值
    df.fillna(0, inplace=True)      # 返回被填充对象的引用
    '''
    fillna函数的参数
        value       填充缺失值的标量值或字典对象
        method      插值方式
        axis        默认为0
        inplace     修改调用者对象而不产生副本
        limit       可以连续填充的最大数量
    '''

    pass


def practice_five():
    data = Series(np.randomrandn(10),
                  index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                         [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
    data.index
    data['b']
    data['b':'c']
    data.ix[['b', 'd']]
    data[:, 2]
    data.unstack()
    data.unstack().stack()

    # 重排分级顺序
    frame = DataFrame(np.arange(12).reshape((4, 3)),
                      index=[['a', 'a', 'b' ,'b'], [1, 2, 1, 2]],
                      columns=[['O', 'O', 'C'],
                               ['G', 'R', 'G']])
    frame.index.names = ['key1', 'key2']
    frame.columns.names = ['state', 'color']
    frame.swaplevel('key1', 'key2')
    frame.sortlevel(1)
    frame.swaplevel(0, 1).sortlevel(0)

    # 根据级别汇总统计
    frame.sum(level='key2')
    frame.sum(level='color', axis=1)

    pass

'''
其他
    整数索引
    面板数据
'''

