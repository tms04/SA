import numpy as np

revenues = np.array([374.80, 115.89, 102.96, 93.08, 91.91, 82.75, 79.54, 71.88, 63.13])

data_range = np.max(revenues) - np.min(revenues)

population_variance = np.var(revenues)

population_std_dev = np.std(revenues, ddof=0)  # Ensure population std deviation

Q1 = np.percentile(revenues, 25)
Q3 = np.percentile(revenues, 75)
IQR = Q3 - Q1

walgreens_revenue = 82.75
mean = np.mean(revenues)
z_score_walgreens = (walgreens_revenue - mean) / population_std_dev

# Print results with two decimal places
print(f"{data_range:.2f} is the range")
print(f"{population_variance:.2f} is the variance")
print(f"{population_std_dev:.2f} is the std_dev")
print(f"{IQR:.2f} is the IQR")
print(f"{z_score_walgreens:.2f} is the z_score")