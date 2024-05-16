import pandas as pd
from chart import Chart

df = pd.read_csv('../../douyin_dataset.csv')
del df['Unnamed: 0']
item_df = pd.read_csv('../../作品特征.csv')

bins = [-1, 0, 1, 3, 5, 10, 35]
item_df['点赞等级'] = pd.cut(item_df['点赞量'], bins, labels=[f'({bins[x]}, {bins[x+1]})' for x in range(len(bins)-1)], right=False)
data = item_df.groupby('点赞等级')['点赞量'].sum().reset_index().values.tolist()

title = "点赞数分布"
chart = Chart(title, data)
pie = chart.pie_chart()
pie.render("item_liked_portion_pie_chart.html")