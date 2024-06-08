import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
from sklearn import ensemble
from sklearn.model_selection import GridSearchCV

import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 20

# 数据读取
df = pd.read_csv('douyin_dataset.csv')
del df['Unnamed: 0'], df['H'], df['date'], df['finish'], df['channel']
# print(df.head())

# 数据抽样处理
df_like = df[df['like'] == 1]
df_dislike = df[df['like'] == 0]
data = pd.concat([df_like[::20], df_dislike[::40]], axis=0)
# print(len(data)/len(df))

# 对时间数据进行处理
flag = pd.to_datetime('2019-01-01 00:00:00')
data['real_time'] = pd.to_datetime(data['real_time'])
data['real_time'] = pd.to_timedelta(data['real_time'] - flag).dt.total_seconds()
# print(data.head())

# 数据集划分
xtrain, xtest, ytrain, ytest = train_test_split(
    data.drop('like', axis=1),  # X
    data['like'], test_size=0.3,  # Y
    random_state=0  # random seed为0
)
# print(len(xtrain))
# print(len(xtest))

# 模型训练
def train(name, model):
    # 训练模型
    model = model.fit(xtrain, ytrain)
    # 测试模型
    print(f'{name}准确率: \t{model.score(xtest, ytest)}')
    return model

# 逻辑回归
lgs = train('lgs', LogisticRegression(solver='liblinear', C=100.0, random_state=1))

# 朴素贝叶斯
gnb = train('gnb', GaussianNB().fit(xtrain, ytrain))

# 单棵决策树
clf = train('clf', DecisionTreeClassifier(class_weight='balanced', random_state=0))

# 随机森林
rfc = train('rfc', RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=0))

def my_auc(model):
    y_test_proba = model.predict_proba(xtest)
    false_positive_rate, recall, thresholds = roc_curve(ytest, y_test_proba[:, 1])
    roc_auc = auc(false_positive_rate, recall)
    return false_positive_rate, recall, roc_auc

lgs_auc = my_auc(lgs)
gnb_auc = my_auc(gnb)
clf_auc = my_auc(clf)
rfc_auc = my_auc(rfc)

# 绘制模型的auc曲线
plt.figure(figsize=(6,4), dpi=120)
plt.plot(lgs_auc[0], lgs_auc[1], color='cyan', label='AUC_lgs=%0.3f' % lgs_auc[2])
plt.plot(gnb_auc[0], gnb_auc[1], color='blue', label='AUC_gnb=%0.3f' % gnb_auc[2])
plt.plot(clf_auc[0], clf_auc[1], color='green', label='AUC_clf=%0.3f' % clf_auc[2])
plt.plot(rfc_auc[0], rfc_auc[1], color='yellow', label='AUC_rfc=%0.3f' % rfc_auc[2])
plt.legend(loc='best', fontsize=12,frameon=False)
plt.plot([0,1],[0,1],'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.ylabel('Recall')
plt.xlabel('Fall-out')
plt.savefig('model_auc.png')

# # n_e优化：对n_estimators的优化
# params = {'n_estimators': [x for x in range(100, 1500, 100)]}
# grid = GridSearchCV(
#     RandomForestClassifier(class_weight='balanced', random_state=0),
#     params, scoring='roc_auc',
#     cv=3,verbose=1,n_jobs=-1
# ).fit(xtrain, ytrain)
#
# a = grid.cv_results_['mean_test_score']
# plt.figure(figsize=(6,4),dpi=120)
# plt.plot(params['n_estimators'], a, color='blue')
# plt.savefig('n_e.png')
# print(grid.best_params_)

# params = {
#     'max_features':range(2,10,2)
# }
# grid = GridSearchCV(
#     RandomForestClassifier(n_estimators= 1400, class_weight='balanced', random_state=0),
#     params, scoring='roc_auc',
#     cv=3,verbose=1,n_jobs=-1
# ).fit(xtrain, ytrain)
#
# a = grid.cv_results_['mean_test_score']
# plt.figure(figsize=(6,4),dpi=120)
# plt.plot(params['max_features'], a, color='blue')
# plt.savefig('max_f.png')
# print(grid.best_params_)

# 对优化后的模型进行训练
rfc_best = RandomForestClassifier(n_estimators=1400,
                                  max_features=4,
                                  class_weight='balanced',
                                  random_state=0)
rfc_best = train('rfc++', rfc_best)

# 模型预测
flag = pd.to_datetime('2019-01-01 00:00:00')
df['real_time'] = pd.to_datetime(df['real_time'])
df['real_time'] = pd.to_timedelta(df['real_time'] - flag).dt.total_seconds()

print(rfc_best.score(df.drop('like', axis=1), df['like']))