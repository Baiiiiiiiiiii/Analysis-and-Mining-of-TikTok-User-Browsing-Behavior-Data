import pandas as pd
from chart import Chart

author_df = pd.read_csv('../../作者特征.csv')

bins = [-1, 0, 1, 36]
data = pd.cut(author_df['总点赞量'], bins, right=True, labels=[f'({bins[x]}, {bins[x+1]}]' for x in range(len(bins)-1)]).value_counts().reset_index().sort_values(by='index').values.tolist()


title = "不同点赞量作者占比"
chart = Chart(title, data)
pie = chart.pie_chart()
pie.render("author_liked_portion_pie_chart.html")