import os
import sys
import pandas as pd
from chart import Chart

user_df = pd.read_csv('../../用户特征.csv')

data = user_df['去过的城市数'].value_counts().reset_index().values.tolist()

title = "去过不同城市数量的用户占比"
chart = Chart(title, data)
pie = chart.pie_chart()
pie.render("user_arrive_city_sum_pie_chart.html")