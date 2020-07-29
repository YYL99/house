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


def practice_two():
    np.empty((2, 3, 2))     # 创建一个没有任何具体值的数组，2个数组，分别是3行2列
    a = np.arange(12).reshape(3, 4)
    np.ones_like(a)         # 生成以a为形状的全1数组
    np.zeros_like(a)        # 同上类似
    np.identity(5)          # 生成单位矩阵，同eye不同的是N*N的
    np.array([1, 2, 3], dtype=np.float64)   # 通过dtype=np.float64指定数据类型
    '''
       int8,uint8           有无符号8位整型
       int16,uint16         有无符号16位整型
       int32,uint32         有无符号32位整型
       int64,uint64         有无符号64位整型
       float16              半精度浮点数
       float32              标准的单精度浮点数，与C的float兼容
       float64              标准的双精度浮点数，与C的double和python的float对象兼容
       float128             扩展精度浮点数
       complex64，complex128,complex256 分别用两个32位、64位或128位浮点数表示的复数
       bool                 存储True和False值得布尔类型
       object               python对像类型
       string_              固定长度的字符串类型
       unicode_             固定长度的unicode类型
    '''
    a.dtype                 # 数组显示类型
    a.astype(np.float64)    # 转换数组

    a ** 0.5                # 表示数组的0.5次幂
    # 不同大小的数组之间的运算教做广播
    a[0, 2].copy()          # 对数组进行复制
    arr1 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    arr1[0] = 42            # arr1[0]全为42
    np.random.randn(7, 4)   # 返回一个满足正态分布的七行四列的二维数组
    np.ix_()                # 将两个一维整数数组转换为一个用于选取方形区域的索引器
    np.dot(a.T, a)          # 计算矩阵内积X.T*X
    a.transpose((1,0,2))    # 由轴编号组成的元组才能对这些轴进行转置
    a.swapaxes(1,2)         # 接受一对轴编号


    pass


def practice_three():
    a = np.arange(12).reshape(3, 4)
    np.sqrt(a)              # 简单的元素级变体，一元
    np.exp(a)               # 简单的元素级变体，一元
    np.add()                # 二元
    np.maximum()            # 二元

    pass