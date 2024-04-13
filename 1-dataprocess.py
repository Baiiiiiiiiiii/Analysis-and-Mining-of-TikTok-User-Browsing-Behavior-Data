import pandas as pd
import numpy as np

# 读入数据集
df=pd.read_csv('douyin_dataset.csv')
# 打印数据的前几行
print(df.head())
# 判断数据是否有空缺
print(df.info(null_counts=True))