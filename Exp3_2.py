import numpy as np
 
data = [44, 8, 39, 40, 59, 46, 59, 37, 15, 73, 23, 19, 90, 58, 35, 82, 14, 38, 27, 24, 71, 25, 39, 84, 70]
 
data = np.array(data)
 
Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
 
IQR = Q3 - Q1
 
print(f"Interquartile Range (IQR): {IQR}")