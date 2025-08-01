
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('results.csv')  
plt.boxplot(data)
plt.show()

