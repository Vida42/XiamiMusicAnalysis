# result：data3ac.txt		data3a.txt中只留用户ID并重新排序号

# 转化用户ID

zidian1=[]
with open('data3aa.txt','r', encoding="UTF-8") as f2:
	for each in f2:
		zidian1.append(each.strip())

zidian3 = list(set(zidian1))
zidian3.sort()

total = len(zidian3)+1
zidian2 = [i for i in range(1,total)]

dic = dict(zip(zidian3,zidian2))
#创建字典

a=[]
with open('data3a.txt','r', encoding="UTF-8") as f2:
	for each in f2:
		a.append(each.strip())

b = []
d = []
for each in a:
	b.append(each.split(',')[0])
	d.append(each.split(',')[1])
# b歌曲id,d用户ID串

cx=[]
 
for line in d:  
	linestr = line.strip()
	ax = linestr.split("\t")#将每行分割为列表
	for yuansu in ax:
		ax[ax.index(yuansu)] = dic[yuansu]
	ax.sort()
	ax = list(map(str, ax))#再将列表内int转为str
	bx = '\t'.join(ax)#列表转字符串
	cx.append(bx)#字符串写入cx，即完成原始数据第一行改造

with open ('data3ac.txt','a') as f2:
	for i in cx:
		f2.write(i + '\n')