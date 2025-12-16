from sklearn.linear_model import LinearRegression

# In this function I created a linear regression model
def linearModel(xTrain, yTrain):
    model=LinearRegression()
    model.fit(xTrain,yTrain) # model uses training sets for training.
    return model