# 先把the2按音乐ID排序，再按音乐group
# result: data1.csv       265456条歌曲被用户收藏情况：歌曲，用户

info=[]
with open('the2.txt','r', encoding="UTF-8") as f2:
	for each in f2:
		info.append(each.strip())
# 打开各省包含的风格


a = []
b = []

for x in info:
	a.append(x.split('\t')[0])
	b.append(x.split('\t')[1])


data=[(score, name) for score, name in list(zip(a,b))] #先转化成元组
data.sort() #按照分数排序
a=[score for score,name in data] #将排好序的分数姓名的元组分开
b=[name for score,name in data]

with open ("data0.txt", 'w',encoding = 'utf-8') as f3:
	for i in range(len(a)):
		f3.write(a[i] + ',' + b[i] + '\n')


# 将收藏了同一首歌的用户聚合
import pandas as pd


df = pd.read_csv('data0.txt',names=['song','userID'])
# print(df)
df = df.astype(str) # 将数字转换为字符串
grouped = df.groupby('song')#,as_index=False)
# print(grouped)
result = grouped.agg(lambda x:'+'.join(x))
print(result)
result.to_csv('data1.csv')
