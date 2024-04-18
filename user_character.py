import pandas as pd
import numpy as np


# 读入数据集
df=pd.read_csv('douyin_dataset.csv')
user_df = pd.DataFrame()
# 将所有用户的uid提取为uid列
user_df['uid'] = df.groupby('uid')['like'].count().index.tolist()
# 设置uid列为index，方便后续数据自动对齐
user_df.set_index('uid',inplace=True)
user_df['浏览量'] = df.groupby('uid')['like'].count() # 统计对应uid下的浏览量
user_df['点赞量'] = df.groupby('uid')['like'].sum() # 统计对应uid下的点赞量
user_df['观看作者数'] = df.groupby(['uid']).agg({'author_id':pd.Series.nunique}) # 统计每个用户观看不同作者的数量
user_df['观看作品数'] = df.groupby(['uid']).agg({'item_id':pd.Series.nunique}) # 统计每个用户观看不同作品的数量
user_df['观看作品平均时长'] = df.groupby(['uid'])['duration_time'].mean() # 统计每个用户观看作者的平均时长
user_df['观看配乐数'] = df.groupby(['uid']).agg({'music_id':pd.Series.nunique}) # 统计观看作品中配乐的数量
user_df['完整观看数']  = df.groupby('uid')['finish'].sum() # 统计对应uid下的完整观看数
user_df['去过的城市数'] = df.groupby(['uid']).agg({'user_city':pd.Series.nunique}) # 统计对应uid用户去过的城市数量
user_df['观看作品城市数'] = df.groupby(['uid']).agg({'item_city':pd.Series.nunique}) # 统计每个用户观看的作品涉及的不同城市数量
user_df.describe() # 输出user df的描述性统计，包括均值，标准差等
user_df.to_csv('用户特征.csv', encoding='utf_8_sig') # 保存为csv文件，并且编码为utf-8