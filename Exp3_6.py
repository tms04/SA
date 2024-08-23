import numpy as np
from scipy.stats import norm
 
mean = 419
std_dev = 27

def calculate_bounds(mean, std_dev, num_std_dev):
    lower_bound = mean - num_std_dev * std_dev
    upper_bound = mean + num_std_dev * std_dev
    return lower_bound, upper_bound

lower_68, upper_68 = calculate_bounds(mean, std_dev, 1)
print(f"68% of the figures are between {lower_68:.2f} and {upper_68:.2f} minutes.")

lower_95, upper_95 = calculate_bounds(mean, std_dev, 2)
print(f"95% of the figures are between {lower_95:.2f} and {upper_95:.2f} minutes.")

lower_997, upper_997 = calculate_bounds(mean, std_dev, 3)
print(f"99.7% of the figures are between {lower_997:.2f} and {upper_997:.2f} minutes.")

def percentage_between(lower, upper, mean, std_dev):
    z_lower = (lower - mean) / std_dev
    z_upper = (upper - mean) / std_dev
    pct_lower = norm.cdf(z_lower)
    pct_upper = norm.cdf(z_upper)
    return (pct_upper - pct_lower) * 100
 
lower_bound = 359
upper_bound = 479
pct_between = percentage_between(lower_bound, upper_bound, mean, std_dev)
print(f"Approximately {pct_between:.2f}% of the times are between {lower_bound} and {upper_bound} minutes.")
 
def calculate_z_score(x, mean, std_dev):
    return (x - mean) / std_dev
 
time_spent = 400
z_score = calculate_z_score(time_spent, mean, std_dev)
print(f"Z-score for {time_spent} minutes is {z_score:.2f}.")

print(f"A Z-score of {z_score:.2f} means the worker's time is {abs(z_score):.2f} standard deviations {'below' if z_score < 0 else 'above'} the average.")