import math
import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
from matplotlib.colors import ListedColormap

def generateData(category, num_samples):
    data = []
    u = [0, 0.7, 1.4]
    b = [0.5, 0.7, 0.3]
    for c in range(category):
        sample = np.random.randn(num_samples, 2)*b[c]+u[c]
        for i in range(num_samples):
            data.append([list(sample[i]), c])
    print(data)
    with open("./samples.txt", "w") as f:
        for i in data:
            f.write(str(i) + "\n")
    return data

def showData(traindata, colors):
    classColormap = ListedColormap(colors)
    pl.scatter([traindata[i][0][0] for i in range(len(traindata))],
               [traindata[i][0][1] for i in range(len(traindata))],
               c=[traindata[i][1] for i in range(len(traindata))],
               cmap=classColormap)

def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def gaussCore(u):
    return 1.0/(math.sqrt(2*math.pi))*math.e ** (-0.5 * (u) ** 2)

def PN(testX, trainXY, h, category):
    windowsize = h*1.0/math.sqrt(len(trainXY))
    trainX = [[trainXY[i][0][0], trainXY[i][0][1]] for i in range(len(trainXY))]
    labelX = []
    for i in range(len(trainXY)):
        labelX.append(trainXY[i][1])
    Z_cal = []
    label_inf = []
    num_train = len(trainX)
    for i in range(len(testX)):
        sum = 0.0
        #maxtemp = 0.0
        #flag = 0
        Pn = []
        for o in range(0, category):
            for j in range(o*(int(num_train/category)),(o+1)*(int(num_train/category))):
                temp2 = gaussCore(dist(testX[i], trainX[j])/windowsize)/windowsize
                sum += temp2
            Pn.append(sum/num_train)
        #print(Pn)
        #print(flag)
        label_inf.append(Pn.index(max(Pn)))
        #print(label_inf)
        Z_cal.append((max(Pn)))
    X = testX[:, 0]
    Y = testX[:, 1]
    Z = np.zeros(len(X))
    for i in range(0, len(X)):
        Z[i] = Z_cal[i]
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # ax.scatter(X, Y, Z, c="r")
    # plt.show()
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_trisurf(X, Y, Z, cmap='viridis', edgecolor='none')
    plt.show()
    return label_inf

def calculate_acc(data1, data2):
    return sum([int(data1[i] == data2[i]) for i in range(len(data1))]) / float(len(data1))

def inference(trainXY, testX, testlabel, h, category):
    testWithLabels = []
    testData = np.array(testX)
    textXY_inference = PN(testData, trainXY, h, category)
    for i in range(len(testX)):
        testWithLabels.append([testX[i], textXY_inference[i]])
    a = calculate_acc(textXY_inference, testlabel)
    print("acc =", a)
    return testWithLabels

if __name__ == '__main__':
    # parameters
    category = 3
    h = 10
    print("h =", h)
    num_samples = 500
    num_train = 400
    num_test = 100
    print("train samples' number:", num_train)
    print("test samples' number:", num_test)
    # data = generateData(category, num_samples, sigma)
    new_data = []
    with open("./samples.txt", "r") as f:
        data = f.readlines()
    for i in range(0, len(data)):
        new_data.append(eval(data[i]))
    trainXY1 = new_data[num_samples * 0:num_samples * 0 + num_train]
    trainXY2 = new_data[num_samples * 1:num_samples * 1 + num_train]
    trainXY3 = new_data[num_samples * 2:num_samples * 2 + num_train]
    trainXY = trainXY1 + trainXY2 + trainXY3
    testXY1 = new_data[num_samples * 1 - num_test:num_samples * 1]
    testXY2 = new_data[num_samples * 2 - num_test:num_samples * 2]
    testXY3 = new_data[num_samples * 3 - num_test:num_samples * 3]
    testXY = testXY1 + testXY2 + testXY3

    testlabel = []
    for i in range(len(testXY)):
        testlabel.append(testXY[i][1])
    testX = [[testXY[i][0][0], testXY[i][0][1]] for i in range(len(testXY))]
    res1 = inference(trainXY, testX, testlabel, h, category)
    train_color = ['#CD5555', '#104E8B', '#008B00']
    inference_color = ['#FFC1C1', '#BBFFFF', '#9AFF9A']
    showData(trainXY, train_color)
    showData(res1, inference_color)
    pl.show()
