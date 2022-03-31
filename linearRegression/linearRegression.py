import learn as learn
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


nasdaqFile = "inputFile/nasdaq.csv"
usoFile = "inputFile/uso.csv"
googFile = "inputFile/goog.csv"
xomFile = "inputFile/xom.csv"

def readFile(filename):
    data = pd.read_csv(filename, sep=",", usecols=[0, 6], names=['Date', 'Price'], header=0)
    # print(data.head())
    returns = np.array(data['Price'][:-1], np.float32) / np.array(data['Price'][1:], np.float32) - 1
    data["Returns"] = np.append(returns, np.nan)
    print(data.head())
    return data


googData = readFile(googFile)
usoData = readFile(usoFile)
nasdaqData = readFile(nasdaqFile)
xomData = readFile(xomFile)
