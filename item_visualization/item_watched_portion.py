import pandas as pd
from chart import Chart

df = pd.read_csv('../../douyin_dataset.csv')
del df['Unnamed: 0']
item_df = pd.read_csv('../../作品特征.csv')

bins = [0, 1, 2, 4, 1600]
item_df['浏览量等级'] = pd.cut(item_df['浏览量'], bins, labels=[f'({bins[x]}, {bins[x+1]}]' for x in range(len(bins)-1)])
data = item_df.groupby('浏览量等级')['浏览量'].count().reset_index().values.tolist()

title = "作品浏览量分布"
chart = Chart(title, data)
pie = chart.pie_chart()
pie.render("item_watched_portion_pie_chart.html")