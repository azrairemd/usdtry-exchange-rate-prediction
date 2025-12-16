import matplotlib.pyplot as plt

# to compare actual value and predicted value same time
def plotActualPred(yTrue,yPred, title="Actual Value vs Predicted Value"):
    plt.figure(figsize=(10,5))
    plt.plot(yTrue.index, yTrue, label="Actual")
    plt.plot(yTrue.index, yPred, label="Predicted")
    plt.title(title) # I specified it
    plt.legend()
    plt.show()