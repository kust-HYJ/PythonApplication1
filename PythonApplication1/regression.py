# -*- coding:utf-8 -*-
import numpy as np

def createData(filename):
    fr = open(filename)
    numfeat = len(fr.readline().split('\t')) - 1
    dataMat = []
    labelMat = []
    index = 0
    for line in fr.readlines():
        line = line.strip().split('\t')
        temp = np.array(line[0:numfeat], dtype=float)
        dataMat.append(temp)
        labelMat.append(float(line[-1]))
    return dataMat, labelMat

def standRegres(xArr, yArr):
    '''
    计算行列式是否为0
   
    利用正规方程求解参
    '''
    xMat = np.mat(xArr); yMat = np.mat(yArr).T
    xTx = xMat.T * xMat
    if np.linalg.det(xTx) == 0:     #计算矩阵行列式
        print('这是一个奇异矩阵，不能做逆运算')
        return
    ws = xTx.I * (xMat.T * yMat)
    return ws

def gradientDescent(data, label):
    '''
    利用梯度下降搜索算法拟合参数

    problem：a=0.09时在第255步拟合后，算法不能收敛
             a=0.1时在第92步拟合后，算法不能收敛
    '''
    dataMat = np.mat(data)
    labelMat = np.mat(label)
    a = 0.1        #设置学习速率
    theta0 = 0
    theta1 = 0
    giff0 = 0
    giff1 = 0
    cnt = 0     #迭代次数
    m = len(dataMat)
    while True:
        for i in range(m):
            giff0 += (theta0 + theta1 * dataMat[i, 1] - labelMat[0, i])
            giff1 += ((theta0 + theta1 * dataMat[i, 1] - labelMat[0, i]) * dataMat[i, 1])
        theta0 -= a / m * giff0
        theta1 -= a / m * giff1
        cnt += 1
        if int(theta1*10)==16 and int(theta0*10)==30 :
            break
    return theta0, theta1 
    
def lwlr(testpoint, xArr, yArr, k):
    '''
    局部加权线性回归函数

    '''
    xMat = np.mat(xArr); yMat = np.mat(yArr).T
    m = np.shape(xMat)[0]      #计算xMat的行数
    weights = np.mat(np.eye(m))
    for j in range(m):
        diffMat = testpoint - xMat[j,:]
        weights[j, j] = np.exp(diffMat * diffMat.T / (-2.0 * k ** 2))       #高斯核不理解
    xTx = xMat.T * weights * xMat
    if np.linalg.det(xTx) == 0:
        print('这是一个奇异矩阵')
        return
    ws = xTx.I * (xMat.T * (weights * yMat))
    return testpoint * ws

def lwlrtest(testArr, xArr, yArr, k):
    '''
    用于数据集中的每个点调用lwlr函数，以便求解k

    '''
    m = np.shape(testArr)[0]
    yHat = np.zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i], xArr, yArr, k)
    return yHat
