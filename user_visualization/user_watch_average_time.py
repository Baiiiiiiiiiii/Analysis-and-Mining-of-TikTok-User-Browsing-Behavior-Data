import os
import sys
import pandas as pd
from chart import Chart

user_df = pd.read_csv('../../用户特征.csv')

bins = [1, 10, 12, 15, 42]
data = pd.cut(user_df['观看作品平均时长'], bins, right=True, labels=[f'({bins[x]}, {bins[x+1]}]' for x in range(len(bins)-1)]).value_counts()
data = data.sort_index(ascending=False).cumsum().reset_index().values.tolist()

title = "观看作品平均时长"
chart = Chart(title, data)
pie = chart.fl_chart()
pie.render("user_watch_average_time_fl_chart.html")