import pandas as pd
import numpy as np


# 读入数据集
df = pd.read_csv('../douyin_dataset.csv')
author_df = pd.DataFrame()
author_df['author_id'] = df.groupby('author_id')['like'].count().index.tolist()  # 通过不同author—id对作者进行分类
author_df.set_index('author_id', inplace=True)  # 讲author-id这一列设为索引列
author_df['总浏览量'] = df.groupby('author_id')['like'].count()  # 统计该作者的总浏览量
author_df['总点赞量'] = df.groupby('author_id')['like'].sum()  # 统计该作者的总点赞量
author_df['总观完量'] = df.groupby('author_id')['finish'].sum()  # 统计该作者的总观完量
author_df['总作品数'] = df.groupby('author_id').agg({'item_id': pd.Series.nunique})  # 统计不同作者的总作品数

item_time = df.groupby(['author_id', 'item_id']).mean().reset_index()  # 计算每个作者每个作品的平均时长
author_df['作品平均时长'] = item_time.groupby('author_id')['duration_time'].mean()

author_df['使用配乐数量'] = df.groupby('author_id').agg({'music_id':pd.Series.nunique})  # 统计每个作者使用的配乐数量
author_df['发布作品日数'] = df.groupby('author_id').agg({'real_time':pd.Series.nunique})  # 统计每个作者发布作品的日数

author_days = df.groupby('author_id')['date']
_ = pd.to_datetime(author_days.max()) - pd.to_datetime(author_days.min())
author_df['创作活跃度(日)'] = _.astype('timedelta64[D]').astype(int) + 1  # 作者发布日期的总天数（天数+1）
author_df['去过的城市数'] = df.groupby(['author_id']).agg({'item_city':pd.Series.nunique})  # 作者去过的城市数

author_df.describe()
author_df.to_csv('作者特征.csv', encoding='utf_8_sig')