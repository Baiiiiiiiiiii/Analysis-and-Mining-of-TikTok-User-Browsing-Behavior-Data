import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import pandas as pd
from chart import Chart

user_df = pd.read_csv('../../用户特征.csv')

bins = [-1, 0, 1, 183]
# 使用pd.cut函数将user_df中点赞量这列数据划分到对应bins中的区间
data = pd.cut(user_df['点赞量'], bins, right=True,labels=[f'({bins[x]}，{bins[x+1]}]' for x in range(len(bins)-1)]).value_counts().reset_index().sort_values(by='index').values.tolist()

title = "不同点赞量用户占比"
chart = Chart(title, data)
pie = chart.pie_chart()
pie.render("user_like_pie_chart.html")