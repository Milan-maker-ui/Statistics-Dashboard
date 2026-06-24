import numpy as np
import matplotlib.pyplot as plt
from statistics import mean,median ,mode,stdev

# Step 1 : Create a simple dataset
sales = [ 120, 135, 150, 145, 160, 155, 140, 170, 175, 180, 190, 200, 210, 220, 225]

# Step 2 : Compute Basic Statistics
mean_sales = mean(sales)
median_sales = median(sales)
mode_sales = mode(sales)
std_sales = stdev(sales)

# Step 3 : Display Result
print("Sales Data :" ,sales)
print("\n----Statistical Summary---")
print(f"Mean:{mean_sales:.2f}")
print(f"Median : {median_sales}")
print(f"Mode : {mode_sales}")
print(f"Standard Deviation : {std_sales:.2f}")

# Step 4 : Visualization 
plt.figure(figsize = (10,5))
# Hitogram
plt.subplot(1, 2, 2)
plt.hist(sales, bins =7, color='skyblue', edgecolor='black')
plt.title("Sales Distribution Histogram")
plt.xlabel("Sales")
plt.ylabel("Frequency")
# BoxPlot
plt.subplot(1, 2, 2)
plt.boxplot(sales, patch_artist = True,boxprops = dict(facecolor ='lightgreen'))
plt.title("Sales Boxplot")
plt.ylabel("sales values")

plt.tight_layout()
plt.show()