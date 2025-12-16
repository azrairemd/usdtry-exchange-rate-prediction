from sklearn.ensemble import RandomForestRegressor

# In this function I created a random forest model
def rfModel(xTrain,yTrain):
    model=RandomForestRegressor(random_state=42) # I add random_state=42 for consistency
    model.fit(xTrain,yTrain)
    return model