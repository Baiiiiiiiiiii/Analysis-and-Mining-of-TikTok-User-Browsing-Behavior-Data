import pandas as pd
from chart import Chart

df = pd.read_csv('../../douyin_dataset.csv')
del df['Unnamed: 0']
item_df = pd.read_csv('../../作品特征.csv')

# 根据date列来分类，统计对应的date中不同itemid的数量
data = df.groupby(['date']).agg({'item_id' : pd.Series.nunique}).reset_index().values.tolist()

title = "各日单日作品发布量"
chart = Chart(title, data)
pie = chart.line_chart()
pie.render("item_date_sum_line_chart.html")