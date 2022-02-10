import csv
import statistics

with open('data.csv', newline = '')as f:
    reader = csv.reader(f)
    data = list(reader)
data.pop(0)

total_marks = 0
total_entries = len(data)

for i in data:
    total_marks += float(i[1])
mean = total_marks/total_entries
print("Mean is = "+str(mean))

import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
marks = df["Marks"].to_list()
st_dev = statistics.stdev(marks)
print(st_dev)
fig = px.scatter(df, x = "Student", y = "Marks")
fig.update_layout(shapes = [dict(type = 'line', y0 = mean, y1 = mean, x0 = 0, x1 = total_entries)])
fig.show()