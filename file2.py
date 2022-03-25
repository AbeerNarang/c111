import pandas as pd
import plotly_express 
import plotly.figure_factory as ff
import csv 
import statistics

df = pd.read_csv("data1.csv")
data = df["Math_score"].tolist()
fig = ff.create_distplot([data], ["Math_score"], show_hist = False)
fig.show()

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
std = statistics.stdev(data)

print("The mean is: ", mean)
print("The median is: ", median)
print("The mode is: ", mode)
print("The std is: ", std)