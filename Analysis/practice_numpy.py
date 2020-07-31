# -*- coding: utf-8 -*-

import numpy as np
'''
NumPy: 数组和矢量计算
ndarray,一个具有矢量算术运算和复杂广播能力的快速且节约空间的多维数组
three   通用函数
four    利用数组进行数据处理
five    用于文件输入输出
six     线性代数
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

    # 不同大小的数组之间的运算叫做广播

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
    np.add(a, a)                # 二元
    np.maximum(a, a)            # 二元
    arr = np.random.randn(7) * 5
    np.modf(arr)            # 返回小数部分与整数部分
    '''
    一元ufunc     返回一维数组
        abs,fabs            # 计算整数、浮点数或复数的绝对值；对于非复数值可使用fabs更快
        sqrt                # 计算各元素的平方根，同arr ** 0.5
        square              # 各元素的平方，同arr ** 2
        exp                 # 各元素的指数
        log,log10,log2,log1p    # 自然对数，底数为10的log，底数为2的log，log（1+x） 
        sign                # 各元素的正负号：1正数，0零，-1负数
        ceil                # 各元素的ceiling值，即大于等于该值的最小整数
        floor               # 各元素的floor值，即小于等于该值的最大整数
        rint                # 将各元素值四舍五入到最接近的整数，保留dtype
        modf                # 返回数组的小数与整数部分
        isnan               # 检测是否为空值
        isfinite,isinf      # 检测元素是否为无穷
        cos,cosh,sin,sinh   # 普通型和双曲型三角函数
        tan,tanh
        arccos,arccosh,arcsin   # 反三角函数
        arcsnh,arctan,arctanh
        logical_not         # 计算各元素not x的真值，相当于-arr
    
    二元ufunc     返回二维数组
        add                 # 将数组中对应的元素相加
        subtract            # 从第一个数组中减去第二个数组中元素
        multiply            # 相乘
        divide,floor_divide # 除法或向下圆整除法（丢弃余数）
        power               # 第一个数组中的元素A，第二个数组中的元素B，记为A的B次幂
        maximum,fmax        # 最大值，fmax将忽略NaN
        minimum,fmin        # 最小值，fmin将忽略NaN
        mod                 # 求模计算（除数的余数）
        copysign            # 将第二个数组中的值的符号复制给第一个数组中的值
        greater,greater_equal   # 相当于，>、>=、<、<=、==、!=
        less,less_equal,equal,not_equal
        logical_and,logical_or,logical_xor  # 相当于，&、|、^
    '''

    pass


def practice_four():
    # 假设在一组值上计算函数sqrt(x^2 + y^2)；
    # np.meshgrid函数接受两个一维数组，并产生两个二维矩阵。
    points = np.arange(-5, 5, 0.01)         # 1000个间隔相同的点
    xs, ys = np.meshgrid(points, points)    # 由两个一维数组，产生两个二维数组
    z = np.sqrt(xs ** 2 + ys ** 2)          # 计算sqrt(x^2 + y^2)
    import matplotlib.pyplot as plt         # 导入matplotlib.pyplot
    plt.imshow(z, cmap=plt.cm.gray)         # 使用自定义的colormap（灰度图）;还有plt.cm.cool，plt.cm.hot和默认
    plt.colorbar()                          # 颜色刻度
    plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
    # plt.show()                              # 展示

    xa = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
    ya = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
    cond = np.array([True, False, True, True, False])       # 赋值
    result = [(x if c else y) for x, y, c in zip(xa, ya, cond)]
    result2 = np.where(cond, xa, ya)        # 同上等价；满足cond则xa，不满足则ya
    # print(result, result2)

    arr = np.random.randn(4, 4)         # 4行4列的二维正态分布数组
    np.where(arr > 0, 2, -2)            # 满足arr>0则2，不满足则-2
    np.where(arr > 0, 2, arr)           # 不限于数组，可为其他
    '''
    若如下：
        result = []
        for i in rang(n):
            if cond1[i] and cond2[i]:
                result.append(0)
            elif cond1[i]:
                result.append(1)
            elif cond2[i]:
                result.append(2)
            else:
                result.append(3)
    可等价于：
        np.where(cond1 & cond2, 0,
                    np.where(cond1, 1,
                                np.where(cond2, 2, 3)))
    还可以等价于：
        result = 1 * (cond1 - cond2) + 2 * (cond2 & -cond1) + 3 * -(cond1 | cond2)
    '''
    arr = np.random.randn(5, 4)         # 正态分布
    arr.mean()                          # 求均值
    np.mean(arr)                        # 同上
    arr.sum()                           # 求和;np.sum(arr)
    arr.mean(axis=1)                    # 每一行的均值；axis=0每一列的均值
    arr.sum(0)                          # 每列的和；1每行的和；可写成axis=
    arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    '''cumsum
    0:实现0轴上的累加：以最外面的数组元素为单位，以[[0,1,2]]为开始实现后面元素的对应累加
    1:实现1轴上的累加：以次外层数组元素为单位，实现后面元素的对应累加
    2:实现2轴上的累加：以次次外层的数组元素为累加单位，即1为开始，实现后面的元素累加
    …………
    n:实现2轴上的累加：以最里面的元素为累加单位，实现后面的元素累加
    '''
    arr.cumsum(0)
    arr.cumprod(1)      # 积
    '''
    基本数组统计方法：
        sum             # 和
        mean            # 算术平均数
        std,var         # 标准差和方差
        min,max         # 最小，最大
        argmin,argmax   # 最小索引，最大索引
        cumsum          # 所有元素的累计和
        cumprod         # 所有元素的累计积
    '''

    arr = np.random.randn(100)
    (arr > 0).sum()     # 正数的数量
    bools = np.array([False, False, True, False])
    bools.any()         # 测试数组中是否存在一个或多个True
    bools.all()         # 检查数组中所有值是否都是True

    arr = np.random.randn(8)
    arr.sort()          # 排序，小到大
    arr = np.random.randn(5, 3)
    arr.sort(1)         # 行排序；0列排序

    large_arr = np.random.randn(1000)
    large_arr.sort()
    v = large_arr[int(0.05 * len(large_arr))]   # 5%分位数

    names = np.array(['Bob', 'Joe', 'Will', 'Joe', 'Joe'])
    np.unique(names)        # 集合
    ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
    np.unique(ints)         # 集合

    values = np.array([6, 0, 0, 3, 2, 5, 6])
    np.in1d(values, [2, 3, 6])      # 测试一个数组中的值在另一个数组中的成员资格，返回布尔型数组
    '''
    数组的集合运算：
        unique(x)           # 计算x中的唯一元素，返回有序结果
        intersect1d(x, y)   # 计算x，y中的公共元素，返回有序结果
        union1d(x, y)       # 计算x，y的并集，返回有序结果
        in1d(x, y)          # 得到一个表示“x的元素是否包含于y”的布尔型数组
        setdiff1d(x, y)     # 集合的差，在x中且不在y中
        setxor1d(x, y)      # 集合的对称差，存在于一个数组中但不同时存在于两个数组中
    '''

    pass


def practice_five():
    arr = np.arange(10)
    np.save('some_array', arr)      # 以原始的二进制格式保存，没有扩展名则自动加上.npy
    np.load('some_array.npy')           # 读取文件
    np.savez('array_archive.npz', a=arr, b=arr)   # 以关键字参数的形式传入多个数组
    arch = np.load('array_archive.npz')    # 读取文件
    print(arch['a'])           # arch['a']根据关键字显示内容

    # !type array_ex.txt        在Windows中查看array_ex.txt文件
    np.loadtxt('array_ex.txt', delimiter=',')   # 以，为分隔点，构成数组;txt文件
    np.savetxt()        # 相反的操作，将数组转换为以某种分隔符隔开的文本文件

    pass


def practice_six():
    x = np.array([[1., 2., 3.], [4., 5., 6.]])
    y = np.array([[6., 23.], [-1, 7], [8, 9]])
    x.dot(y)        # == np.dot(x, y)   乘法==x的每行分别乘以y的每列
    np.dot(x, np.ones(3))       # np.ones(3)一维数组

    from numpy.linalg import inv, qr
    X = np.random.randn(5, 5)
    mat = X.T.dot(X)        # X.T为X的转置
    inv(mat)                # inv求逆矩阵
    mat.dot(inv(mat))       # 矩阵与逆矩阵之积为单位矩阵
    q, r = qr(mat)          # QR分解
    '''
    numpy.linalg函数
        diag        # 以一维数组的形式返回方阵的对角线；或将一维数组转换为方阵
        dot         # 矩阵乘法
        trace       # 对角线元素的和
        det         # 矩阵行列式
        eig         # 方阵的本征值和本征向量
        inv         # 方阵的逆
        pinv        # 矩阵的Moore-Penrose伪逆
        qr          # QR分解
        svd         # 奇异值分解
        solve       # 解Ax=b
        lstsq       # Ax=b的最小二乘解
    '''

    pass


def practice_seven():
    np.random.normal(size=(4, 4))       # 标准正态分布的4*4样本数组
    from random import normalvariate
    '''
    numpy.random函数
        seed        # 随机数生成器的种子
        permutation # 返回一个序列的随机排列或随机排列的范围
        shuffle     # 对一个序列就地随机排列
        rand        # 产生均匀分布的样本值
        randint     # 给定范围内随机选取整数
        randn       # 正态分布的样本值
        binomial    # 二项分布的样本值
        normal      # 高斯分布的样本值
        beta        # Beta分布的样本值
        chisquare   # 卡方分布的样本值
        gamma       # Gamma分布的样本值
        uniform     # [0,1)中均匀分布的样本值
    '''

    pass


if __name__ == '__main__':
    # practice_four()

    pass

