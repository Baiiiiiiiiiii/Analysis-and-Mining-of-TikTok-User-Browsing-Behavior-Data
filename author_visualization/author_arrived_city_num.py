import pandas as pd
from chart import Chart

author_df = pd.read_csv('../../作者特征.csv')

bins =[0, 1, 2, 10, 19]
data = pd.cut(author_df['去过的城市数'], bins, right=True, labels=[f'{bins[x]}, {bins[x+1]}]' for x in range(len(bins)-1)]).value_counts().reset_index().values.tolist()

title = "作者去过的城市数量分布"
chart = Chart(title, data)
pie = chart.pie_chart()
pie.render("author_arrived_cities_num_pie_chart.html")