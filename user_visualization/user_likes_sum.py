import os
import sys
import pandas as pd
from chart import Chart

user_df = pd.read_csv('../../用户特征.csv')

# sort_values进行降序排序，重置索引（为了保持连续的整数索引），计算‘点赞量’的累积和
temp = user_df['点赞量'].sort_values(ascending=False).reset_index().cumsum()['点赞量']
# 将累计和除以最大值，使得所有值归一化到0和1之间，为了表示累计和的百分比
temp = temp/temp.max()
data = temp.reset_index().values.tolist()

title = "用户点赞量"
chart = Chart(title, data)
pie = chart.line_chart()
pie.render("user_like_line_chart.html")

# 终端输出不同占比用户的点赞情况
_ = temp.tolist()
for j in range(10):
    j /= 10 # 实际是遍历j从0.0到0.9
    for i in _:
        if i >= j:
            # 如果temp中某个百分比大于或等于j，则在flag中保存这个值，并中断循环
            flag = i
            break
    # 计算达到或者超过j百分比点赞的用户占总用户的比例
    c = _.index(flag) / len(_)
    print(f'{c:4.1%} 的用户点了{j:3.0%} 的赞')