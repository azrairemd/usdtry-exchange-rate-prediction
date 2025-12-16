import pandas as pd # I used pandas to access and proccess on this frame: x = data[['CloseLag1', 'CloseLag2', 'CloseLag3']] 
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from models.linear_regression import linearModel
from data.data import loadData

def prediction(nDays=5,symbol="USDTRY=X"):
    
    # load the data
    data=loadData()

    # feaute and target definition
    x = data[['CloseLag1', 'CloseLag2', 'CloseLag3']]  
    y = data['Close']

    # create a linear regression model
    model=linearModel(x,y)

    # recursive prediction
    lastDays=x.iloc[-1].values # acces dataframe x's last values as numeric 
    predictions=[] 

    for i in range(nDays):
        yPred = model.predict([lastDays])[0] # access this index, then make prediction
        predictions.append(yPred)
        lastDays = np.array([lastDays[1], lastDays[2], float(yPred)]) # update the lastDay array for feautre predictions

    
    # last 30 days for visualization
    lastMonth = data.index[-30:]
    lastMonthClose = data['Close'][-30:]

    lastDate = data.index[-1]
    lastValue = data['Close'].iloc[-1]

    # bridge dates (INCLUDING last actual date)
    predDates = pd.date_range(start=lastDate, periods=nDays + 1, freq='D')
    predValues = [lastValue] + predictions

    # plot
    plt.figure(figsize=(12,6))
    plt.plot(lastMonth, lastMonthClose, label='Actual', linewidth=2)
    plt.plot(predDates, predValues, label='Prediction', linewidth=2)

    plt.title(f'{symbol} Next {nDays} Days Prediction')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return predictions 