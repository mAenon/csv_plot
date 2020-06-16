import matplotlib.pyplot as plt
import pandas as pd
import os
import re
import numpy as np

# 開くファイル指定

path = input("data folder path?")
if path == "":
    path = "./"
if path[-1] != "/":
    path += "/"

_list = os.listdir(path)

csv_list = []
for name in _list:
    if re.fullmatch(".+\.csv", name):
        # 正規表現 csvファイルget
        csv_list.append(name)
for i, name in enumerate(csv_list):
    print(i, ":", name)

num = int(input("which csv file open? type num : "))
try:
    path = path + csv_list[num]
    print("open :", path)
except Exception:
    print("error")
    exit()

    # フレームサイズ指定, numpy配列に格納
"""
frame_size = int( input ("frame size?") )
# data = np.loadtxt(path, delimiter=",").reshape(-1, frame_size, 3)
# ここはデータに応じて書き換える必要がある．
"""

# hasc で取ってきた個人の一つのデータならこれ
# data frame でやるパターン
# python ファイルで実行すると汚いx
"""
data = pd.read_csv(path, header=None, names=[
                   "time", "x", "y", "z"], index_col=0)
data.head()
data.plot(figsize=(7, 4))

data.plot(subplots=True, layout=(3, 1), sharex=True, sharey=True)
"""

# np でやるパターン
numarray = np.loadtxt(path, delimiter=",")
print(numarray.shape)

plt.plot(numarray[:, 1], label="x")
plt.plot(numarray[:, 2], label="y")
plt.plot(numarray[:, 3], label="z")
plt.legend()
plt.show()


plt.figure(figsize=(15, 10))
plt.subplot(3, 1, 1)
plt.plot(numarray[:, 0], numarray[:, 1], label="x")

plt.subplot(3, 1, 2)
plt.plot(numarray[:, 0], numarray[:, 2], label="y", color="orange")

plt.subplot(3, 1, 3)
plt.plot(numarray[:, 0], numarray[:, 3], label="z", color="green")

plt.show()
