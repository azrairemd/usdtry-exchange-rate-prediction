import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from utils.split import split
from utils.plotting_regression import plotActualPred
from utils.error import rmse
from models.linear_regression import linearModel
from data.data import loadData

# load the data
data = loadData()

# feaute and target definition
x=data[['CloseLag1','CloseLag2','CloseLag3']]
y=data['Close']

# split the dataset into training and test sets
xTrain, xTest, yTrain, yTest = split(x,y)

# create linear regression model
model = linearModel(xTrain,yTrain)

# make predictions on the test data
yPred=model.predict(xTest) # model makes predictions based on features
# calculate the error
error=rmse(yTrue=yTest, yPred= yPred)
print("RMSE:",error)

# naive baseline: tomorrow=today
yNaive=xTest['CloseLag1']
naiveError=rmse(yTest,yNaive)
print("Naive RMSE:",naiveError)

# which model is better? Naive or LR
improvement=(naiveError- error)/naiveError*100
print("Improvement: %",improvement)

# plot
plotActualPred(yTest, yPred) # yTest is real value and yPred is model's prediction



'''
When this file is executed, the model produces a plot
("assets/linear_regression_train_graph.png") and an RMSE value
of 0.10265913802536196.

Considering that the target variable (USD/TRY exchange rate)
has values approximately between 35 and 42, this RMSE value
is relatively small compared to the scale of the data.

This indicates that the linear regression model is able to
predict future values with a low average error.
Additionally, since the data is split chronologically without shuffling,
the RMSE reflects the model’s performance on future (unseen) data.
'''