import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from data.data import loadData
from utils.split import split
from utils.plotting_regression import plotActualPred
from utils.error import rmse
from models.random_forest import rfModel

# load the data
data = loadData()

# feaute and target definition
x=data[['CloseLag1','CloseLag2','CloseLag3']]
y=data['Close']

# split the dataset into training and test sets
xTrain, xTest, yTrain, yTest = split(x,y)

# create a random forest model
model = rfModel(xTrain,yTrain)

# make predictions on the test data
yPred=model.predict(xTest) # model makes predictions based on features

# plot
plotActualPred(yTest, yPred) # yTest is real value and yPred is model's prediction

# calculate the error
error=rmse(yTrue=yTest, yPred= yPred)
print("RMSE:",error)

'''
As shown in assets/random_forest_train_graph.png, 
the Random Forest model achieves a high RMSE of 4.61
and fails to follow the upward trend and sudden changes 
in the USD/TRY time series.

Random Forest underperformed due to its inability to 
extrapolate in trending time series.
'''