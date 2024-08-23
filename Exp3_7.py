import numpy as np
import pandas as pd
from scipy import stats
 
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
data = pd.read_csv(url, names=columns)
 
sample = data['petal_length'].sample(10, random_state=1)  
 
variance = np.var(sample, ddof=1)
std_deviation = np.std(sample, ddof=1)  
 
z_scores = stats.zscore(sample)
 
print(f"Sample Data:\n{sample}\n")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_deviation}")
print(f"Z-scores:\n{z_scores}")