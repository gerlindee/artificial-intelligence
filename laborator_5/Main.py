import matplotlib as mpl
import matplotlib.pyplot
import pandas as pd

from ActivationFunctions import *
from Network import Network


def test():
    nn = Network([40, 20, 10, 1], ReLU, derr_ReLU)
    file = r'CTG-values.xls'
    df = pd.read_excel(file)
    noIter = 1000
    total = 2100
    errors = []
    iterations = []
    for i in range(noIter):
        iterations.append(i)
        e = []
        output = df['NSP'][i]
        inputs = [df['b'][i], df['e'][i], df['AC'][i], df['FM'][i], df['UC'][i], df['DL'][i], df['DS'][i], df['DP'][i],
                  df['DR'][i], df['LB'][i], df['AC1'][i], df['FM1'][i], df['UC1'][i], df['DL1'][i], df['DS1'][i],
                  df['DP1'][i], df['ASTV'][i], df['MSTV'][i], df['MLTV'][i], df['Width'][i], df['Min'][i], df['Max'][i],
                  df['Nmax'][i], df['Nzeros'][i], df['Mode'][i], df['Mean'][i], df['Median'][i], df['Variance'][i],
                  df['Tendency'][i], df['A'][i], df['B'][i], df['C'][i], df['D'][i], df['E'][i], df['AD'][i],
                  df['DE'][i], df['LD'][i], df['FS'][i], df['SUSP'][i], df['CLASS'][i]]
        e.append(nn.computeLoss(inputs, output)[0])
        nn.backPropag(nn.computeLoss(inputs, output), 0.00000000001)
        errors.append(sum([x ** 2 for x in e]))
    output = df['NSP'][2000]
    inputs = [df['b'][2000], df['e'][2000], df['AC'][2000], df['FM'][2000], df['UC'][2000], df['DL'][2000],
              df['DS'][2000], df['DP'][2000], df['DR'][2000], df['LB'][2000], df['AC1'][2000], df['FM1'][2000],
              df['UC1'][2000], df['DL1'][2000], df['DS1'][2000], df['DP1'][2000], df['ASTV'][2000],
              df['MSTV'][2000],
              df['MLTV'][2000], df['Width'][2000], df['Min'][2000], df['Max'][2000], df['Nmax'][2000],
              df['Nzeros'][2000], df['Mode'][2000], df['Mean'][2000], df['Median'][2000], df['Variance'][2000],
              df['Tendency'][2000], df['A'][2000], df['B'][2000], df['C'][2000], df['D'][2000], df['E'][2000],
              df['AD'][2000], df['DE'][2000], df['LD'][2000], df['FS'][2000], df['SUSP'][2000], df['CLASS'][2000]]
    mpl.pyplot.plot(iterations, errors, label='loss value / iteration')
    mpl.pyplot.xlabel('ITERATIONS')
    mpl.pyplot.ylabel('LOSS VALUE')
    mpl.pyplot.legend()
    mpl.pyplot.show()

test()