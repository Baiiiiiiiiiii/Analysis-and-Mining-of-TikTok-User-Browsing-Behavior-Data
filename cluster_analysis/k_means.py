import numpy as np
import pandas as pd


from pyecharts.charts import *
from pyecharts import options as opts

from sklearn.cluster import KMeans
import joblib
from sklearn import metrics
from scipy.spatial.distance import cdist

# 数据读取
user_feature = pd.read_csv('../用户特征.csv', index_col=0)
author_feature = pd.read_csv('../作者特征.csv', index_col=0)

# 数据处理
# 筛选至少看过一个完整视频且有一定的浏览量的用户
user_data = user_feature[(user_feature['完整观看数'] >= 1) & (user_feature['浏览量'] >= 5)]
print(len(user_data))  # 42040
print(len(user_data)/len(user_feature))  # 0.71

# 筛选具有一定浏览量的作者
author_data = author_feature[(author_feature['总观完量'] >= 1) & (author_feature['总浏览量'] >= 3)]
print(len(author_data))  # 62253
print(len(author_data)/len(author_feature))  # 0.30


def km(data, name):
    K = range(2, 10)
    X = data
    # sc : 轮廓系数。sse：误差平方和
    scores = {'sc': [], 'sse': []}
    for _k in K:
        kmeans = KMeans(n_clusters=_k, init='k-means++', random_state=0)
        kmeans.fit(X)  # 训练模型
        _y = kmeans.predict(X)  # 预测每个数据点的聚类标签

        # 计算评估指标
        sse = sum(np.min(cdist(X, kmeans.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0]  # 误差平方和
        sc = metrics.silhouette_score(X, _y)  # 轮廓系数
        # 将训练好的Kmeans模型保存到文件里
        joblib.dump(kmeans, f'{name}{_k}聚类.model')

        scores['sse'].append(sse)
        scores['sc'].append(sc)
        print(f"聚{_k}类计算完成", end="\t")

    # 将scores字典保存到文件
    joblib.dump(scores, f'{name}聚类指标.score')
    print("指标存储完毕")
    return scores

def draw(k, sse, sc):
    chart = (
        Line(init_opts=opts.InitOpts(
            theme='light',
            width='350px',
            height='350px',
        ))
        .add_xaxis(k)
        .add_yaxis('sse', sse, yaxis_index=0, label_opts=opts.LabelOpts(is_show=False))
        .add_yaxis('sc', sc, yaxis_index=1, label_opts=opts.LabelOpts(is_show=False))
        # 一共有两个y轴，扩展一下y轴选项
        .extend_axis(yaxis=opts.AxisOpts())
        # 设置全职选项
        .set_global_opts(
            title_opts=opts.TitleOpts(title="聚类效果"),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=True),
            yaxis_opts=opts.AxisOpts(
                # 表示y轴类型为数值型
                type_="value",
                # 显示轴刻度
                axistick_opts=opts.AxisTickOpts(is_show=True),
                # 显示分割线
                splitline_opts=opts.SplitLineOpts(is_show=True)
            ),
        )
    )
    return chart

# 模型训练
# user_score = km(user_data, '用户')

# 选择聚类k值，k值是从2到9，因为k值越大，对应的聚类精度越高，但是计算复杂度也会增加
# user_score = joblib.load(f"用户聚类指标.score")
# # 着重看sc曲线，因为sc体现了聚类效果
# chart = draw([str(x) for x in range(2,10)], user_score['sse'], user_score['sc'])
# chart.render("用户聚类指标.html")

# 聚类结果
# user_km = joblib.load(f'用户4聚类.model')  # 加载k=4的训练完毕的模型
# user_centers = pd.DataFrame(user_km.cluster_centers_, columns=user_feature.columns)  # 构造结果的数据结构框架
# # 首先用模型进行聚类，然后对每个聚类进行计数，然后将每个聚类的人数包装为一个Series对象，并作为新的一列添加到user_centers中
# user_centers['人数'] = pd.Series(user_km.predict(user_data)).value_counts()
# print(user_centers)

# 作者模型训练
# author_score = km(author_data, '作者')

# 聚类K值选择
# author_score = joblib.load(f'作者聚类指标.score')
# chart = draw([str(x) for x in range(2, 10)], author_score['sse'], author_score['sc'])
# chart.render("作者聚类指标.html")

# 聚类效果
author_km = joblib.load(f'作者8聚类.model')
author_centers = pd.DataFrame(author_km.cluster_centers_, columns=author_feature.columns)
author_centers['人数'] = pd.Series(author_km.predict(author_data)).value_counts()
print(author_centers)

