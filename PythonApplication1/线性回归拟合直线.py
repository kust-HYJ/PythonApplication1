## -*- coding:utf-8 -*-
#import numpy as np
#import regression
#import matplotlib.pyplot as plt

#xArr, yArr = regression.createData('ex0.txt')
#ws = regression.standRegres(xArr, yArr)
#xMat = np.mat(xArr)
#yMat = np.mat(yArr)
#yHat = xMat*ws

#xgxs = np.corrcoef(yHat.T, yMat)       #corrcoef函数可以计算相关系数
#print(xgxs)
#a, b = regression.gradientDescent(xArr, yArr)
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.scatter(xMat[:, 1], yMat.T[:, 0])
#ax.plot(xMat[:, 1], a+b*xMat[:, 1],c = 'red')
#plt.show()      #线性回归拟合直线

#yHat1 = regression.lwlrtest(xArr, xArr, yArr, 0.01)
#srtInd = xMat[:, 1].argsort(0)      #按升序排序，并返回下标
#xSort = xMat[srtInd][:, 0]    #将xMat按照升序排序
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.plot(xSort[:, 1], yHat1[srtInd],c = 'red')
#ax.scatter(xMat[:, 1], yMat.T[:, 0])
#plt.show()
number = int(input('请输入一个整数：'))
print(number)