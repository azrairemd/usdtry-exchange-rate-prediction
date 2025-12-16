# the dataset is splitted into train and test set
def split(x,y,test_size=0.3):
    splitIndex=int(len(x)*(1-test_size)) 

    xTrain=x[:splitIndex]
    xTest=x[splitIndex:]
    yTrain=y[:splitIndex]
    yTest=y[splitIndex:]

    return xTrain, xTest, yTrain, yTest

'''
I initially used train_test_split from sklearn.
But it shuffles the data, this is not suitable for time series.
In time series the data must be split into past (training) and future (testing).
'''

'''
xTrain and yTrain used for learning
and xTest and yTest used for prection
'''