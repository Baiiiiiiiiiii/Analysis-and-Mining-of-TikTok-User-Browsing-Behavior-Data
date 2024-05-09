import os
import sys
import pandas as pd
from chart import Chart

user_df = pd.read_csv('../../用户特征.csv')

bins = [0, 5, 10, 20, 30, 50, 284]
data = pd.cut(user_df['完整观看数'], bins, right=True, labels=[f'({bins[x]}, {bins[x+1]}]' for x in range(len(bins)-1)]).value_counts().reset_index().values.tolist()

title = "完整观看情况"
chart = Chart(title, data)
pie = chart.pie_chart()
pie.render("user_finish_watch_line_chart.html")