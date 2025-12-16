''' data retrieval and basic preprocessing'''
import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime

def loadData():
    today=datetime.now().strftime("%Y-%m-%d") # This line ensures the currrent date
    startDate="2023-01-01"

    data = yf.download("USDTRY=X", start=startDate, end=today)
    data = data[['Close']]
        
    # feature selection
    data=data[['Close']]

    # add extra features
    # I used these to track a serie
    data['CloseLag1']=data['Close'].shift(1) # 1 day before
    data['CloseLag2']=data['Close'].shift(2) # 2 day before
    data['CloseLag3']=data['Close'].shift(3) # 3 day before

    data=data.dropna()

    return data