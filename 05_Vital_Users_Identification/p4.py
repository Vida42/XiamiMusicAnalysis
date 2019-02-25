# result：data3a.txt       按每首歌曲收藏用户量从少到多排序：歌曲，用户

# 根据收藏用户数，对歌曲排序，先列出现少的
a=[]
with open('data3.txt','r', encoding="UTF-8") as f2:
	for each in f2:
		a.append(each.strip())

b = []
d = []
for each in a:
	b.append(each.split(',')[0])
	d.append(each.split(',')[1])
# b歌曲id,d用户ID串

c=[]
for i in d:
	c.append(i.count('\t'))
# 统计每首歌下的用户数

b2 = []
d2 = []

data=[(score, name, name2) for score, name, name2 in list(zip(c,b,d))] #先转化成元组
data.sort() #按照每首歌下的用户数排序
c=[score for score,name,name2 in data] #将排好序的元组分开
b=[name for score,name,name2 in data]
d=[name2 for score,name,name2 in data] 


with open ("data3a.txt", 'w',encoding = 'utf-8') as f3:
	for i in range(len(a)):
		f3.write(b[i] + ',' + d[i] + '\n')