# # 现在需要将每一行数据存为一个list，做变化，再保存数据
#result: data1b.txt      1a(只取用户部分的data1)内按用户ID从小到大排序

# cx=[]

# with open('data1a.txt','r') as f:  
# 	for line in f.readlines():  
# 		linestr = line.strip()  
# 		# print (linestr)#将一行先当成一个元素
# 		ax = linestr.split("+")#将每行分割为列表
# 		ax = list(map(int, ax))#列表内str转为int
# 		ax.sort()#列表内排序
# 		ax = list(map(str, ax))#再将列表内int转为str
# 		# print (ax)
# 		bx = '\t'.join(ax)#列表转字符串
# 		# print(bx)
# 		cx.append(bx)#字符串写入cx，即完成原始数据第一行改造

# with open ('data1b.txt','a') as f2:
# 	for i in cx:
# 		f2.write(i + '\n')
