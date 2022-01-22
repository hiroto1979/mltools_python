#!/usr/bin/env python3


import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
%matplotlib inline
import seaborn as sns

# 部分的なheatmap
# 一般的に相関係数が0.95以上のものはいずれかを削除する
def corrmap(features, figsize=(0, 0), bound=95, annot=None):
    if figsize == (0, 0):
        figsize = (len(features)/2, len(features)/3)
    cmap = ListedColormap(['blue', 'aqua', 'whitesmoke', 'yellow', 'red', 'black'])
    bounds = [-100, -bound, -90, 90, bound, 100, 101]
    norm = BoundaryNorm(bounds,cmap.N)
    pd.options.display.float_format = '{:.1f}'.format
    corr_sub = df[features].corr() * 100
    display(corr_sub)
    print("")
    print("bound: {}%".format(bound))
    print("")
    f, ax = plt.subplots(figsize=figsize)
    sns.heatmap(corr_sub, cmap=cmap,norm=norm, vmin=min(bounds), vmax=max(bounds), annot=annot)


# カテゴリデータの可視化
def bar_plots(col, data, figsize=(18, 6)):
    fig = plt.figure(figsize=figsize)
    ax1 = fig.add_subplot(1, 3, 1)   # 1行3列の1番目
    ax1 = sns.countplot(x=col, hue=None, data=df, alpha=0.5)
    ax1.set_title("total")
    
    ax2 = fig.add_subplot(1, 3, 2)   # 1行3列の2番目
    ax2 = sns.countplot(x=col, hue="isTest", data=df, alpha=0.5)
    ax2.set_title("train/test")

    ax3 = fig.add_subplot(1, 3, 3)   # 1行3列の3番目
    ax3 = sns.countplot(x=col, hue="isFraud", data=df_train, alpha=0.5)
    ax3.set_title("isFraud")

    plt.tight_layout()
    plt.show()