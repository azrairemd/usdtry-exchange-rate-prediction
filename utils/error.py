from sklearn.metrics import mean_squared_error
import numpy as np
 
# This function return error value
def rmse(yTrue, yPred):
    return np.sqrt(mean_squared_error(yTrue,yPred))
