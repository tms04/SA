import numpy as np
import scipy.stats as stats
 
data = [41, 15, 31, 25, 24, 23, 21, 22, 22, 18, 30, 20, 19, 19, 16,
        23, 27, 38, 34, 24, 19, 20, 29, 17, 23]
 
mean_value = np.mean(data)
median_value = np.median(data)
 
std_deviation = np.std(data, ddof=1)
 
skewness = 3 * (mean_value - median_value) / std_deviation
 
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Standard Deviation: {std_deviation}")
print(f"Pearsonian Coefficient of Skewness: {skewness}")