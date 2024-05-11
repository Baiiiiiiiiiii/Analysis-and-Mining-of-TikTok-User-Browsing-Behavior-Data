import pandas as pd
from chart import Chart

author_df = pd.read_csv('../../作者特征.csv')

temp = author_df['总点赞量'].sort_values(ascending=False).reset_index().cumsum()['总点赞量'].reset_index()
# 归一化
temp = temp / temp.max()
# lambda表达式
temp['index'] = temp['index'].apply(lambda x: format(x, '.2%'))
data = temp[temp['总点赞量'] < 0.99].values.tolist()


# title = "作者累积点赞量"
# chart = Chart(title, data)
# pie = chart.line_chart()
# pie.render("author_liked_sum_line_chart.html")
_ = temp['总点赞量'].tolist()
for j in range(10):
    j /= 10
    for i in _:
        if i >= j:
            flag = i
            break
    c = _.index(flag) / len(_)
    print(f'{c:4.1%} 的作者获得了{j:3.0%} 的赞')