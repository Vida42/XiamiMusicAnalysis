# result：data3.txt        挑一万个歌：歌曲，用户

# 随机生成10000个整数，挑选在列表中位置等于这些的歌曲与相应用户
import random

total = 265457
population = [i for i in range(total)]
num = 10000
result = random.sample(population, num)
# 随机生成num个population中的数，不重复
print(result)

# 按如上挑10000个
a=[]
with open('data1b.txt','r', encoding="UTF-8") as f2:
	for each in f2:
		a.append(each.strip())
# 打开用户


b = []
with open('data4.txt','r', encoding="UTF-8") as f2:
	for each in f2:
		b.append(each.split(',')[0].strip())
# data4是去掉表头的data1，表示歌曲id

with open ("data3.txt", 'w',encoding = 'utf-8') as f3:
	for i in range(len(result)):
		f3.write(b[result[i]] + ',' + a[result[i]] + '\n')