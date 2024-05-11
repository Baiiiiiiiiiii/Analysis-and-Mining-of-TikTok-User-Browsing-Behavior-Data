import pandas as pd
from chart import Chart

author_df = pd.read_csv('../../作者特征.csv')

bins = [0, 1, 5, 10, 20, 50, 2648]
data = pd.cut(author_df['总浏览量'], bins, right=True, labels=[f'({bins[x]}, {bins[x+1]}]' for x in range(len(bins)-1)]).value_counts().reset_index().values.tolist()

title = "不同浏览量作者占比"
chart = Chart(title, data)
pie = chart.pie_chart()
pie.render("author_watched_portion_pie_chart.html")