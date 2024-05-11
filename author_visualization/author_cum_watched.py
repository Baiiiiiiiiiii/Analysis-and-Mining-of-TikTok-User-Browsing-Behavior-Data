import pandas as pd
from chart import Chart

author_df = pd.read_csv('../../作者特征.csv')

temp = author_df['总浏览量'].sort_values(ascending=False).reset_index().cumsum()['总浏览量'].reset_index()
# 归一化
temp = temp / temp.max()
# 保存小数点后两位
temp['index'] = temp['index'].apply(lambda x: format(x, '.2%'))
data = temp[temp['总浏览量'] < 0.90].values.tolist()

title = "作者累积浏览量占比"
chart = Chart(title, data)
pie = chart.line_chart()
pie.render("author_cum_watched_portion_line_chart.html")