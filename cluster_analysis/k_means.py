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