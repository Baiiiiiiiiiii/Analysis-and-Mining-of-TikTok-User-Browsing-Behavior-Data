import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import pandas as pd
from chart import Chart

user_df = pd.read_csv('../../用户特征.csv')

bins=[0,5,10,25,50,100,1951]  # 浏览量区间
# 根据浏览量区间，将不同浏览量的用户分配到不同的区间里，最后将结果输出为一个列表
data = pd.cut(user_df['浏览量'], bins, right=True, labels=[f'({bins[x]},{bins[x+1]}]' for x in range(len(bins)-1)]).value_counts().reset_index().values.tolist()
title = "不同浏览量用户占比"
chart = Chart(title,data)
pie = chart.pie_chart()
#pie.render("user_browsing_pie_chart.html")  # 将饼状图输出为一个html文件

temp = user_df['浏览量'].sort_values(ascending=False).reset_index().cumsum()['浏览量']  # 将用户浏览量降序排序，并计算累积和
temp = temp/temp.max()  # 累积归一化
data = temp.reset_index().values.tolist()  # 将数据转化为列表，列表中每个元素代表累积百分比的数据点，包含了索引和累积百分比

title = "用户累积浏览量占比"
chart = Chart(title,data)
line_chart = chart.line_chart()
#line_chart.render("user_browsing_line_chart.html")