# -*- coding: utf-8 -*-

import numpy as np
'''
NumPy: 数组和矢量计算
ndarray,一个具有矢量算术运算和复杂广播能力的快速且节约空间的多维数组
'''


def practice_one(d: list):
    # d = [1, 2, 3, 4]      # 创建列表
    a = np.array(d, d)      # 创建数组
    np.zeros(shape=(3, 4))  # 全0的数组
    np.ones(shape=(3, 4))   # 全1
    np.eye(3, 4)            # 单位矩阵
    np.arange(1, 10, 0.5)   # 生成数组，以0.5为间隔，支持浮点数float
    np.arange(1, 10).reshape(3, 3)  # 生成数组，3行3列
    np.random.rand(10)      # 返回10个0-1之间的数据
    np.random.randn(10)     # 返回10个服从标准正态分布的数据
    np.random.randint(10)   # 返回0-9之间任意整数

    t1 = a.ndim     # 查看数组维度
    t2 = a.shape    # 查看数组大小
    t3 = a.size     # 查看数组元素的总数
    t3 = a.dtype    # 查看数组类型

    # 访问数组
    a[0][0]
    a[0, 0]
    a[1:,0:]    # 前为行，后为列

    a = np.arange(12).reshape(3, 4)
    b = np.arange(12).reshape(4, 3)
    # ab数组之间可以直接相加减乘除，但除时不得带0

    matrix_a = np.matrix(a)     # 转换为矩阵
    matrix_b = np.matrix(b)
    # 可加减乘，在乘时，必须A的行数与B的列数相同
    matrix_a.dot(matrix_b)      # 乘法.dot()

    np.concatenate([a,b], axis=0)   # axis=0垂直方向堆叠数组，axis=1水平方向堆叠数组
    np.vstack([a,b])    # 列数相同，垂直...    ab皆是象征
    np.hstack([a,b])    # 行数相同，水平...    ab皆是象征

    ary = np.arange(9)
    np.split(ary, 3)        # 均匀分割
    np.split(ary, [2,5])    # 分为0-2，2-5，5-...
    np.split(a, 2, axis=0)  # 水平分割
    np.split(a, 2, axis=1)  # 垂直分割

    np.sum(ary)         # 一维
    np.min(ary)
    np.max(ary)
    np.sum(a,axis=0)    # 多维
    np.sum(a, axis=1)
    np.min(a,axis=0)
    np.max(a,axis=0)
    np.mean(a,axis=0)   # 均值

    np.percentile(a, q=100) # 分位数

    np.argmin(ary)          # 最小值对应的索引

    np.random.shuffle(a)    # 打乱数组排序
    np.sort(a, axis=0)      # 从小到大排序

    a[0, [True,False,False,True]]
    a[(a >=3) & (a < 10)]


    pass

