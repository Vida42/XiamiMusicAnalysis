# _*_ coding:utf-8 _*_ 


# 共325000000名用户
# 均匀随机抽取325万用户
# 分成100份，每325万取32500名用户，存于Xu2

import random  


multiple = 3250000

for block in range(1,101):
	a = multiple * (block - 1) + 1
	b = multiple * block
	# 在a到b范围，生成32500个数，整数
	res = [random.randint(a, b) for _ in range(1, 32501)]
	with open('Xu2_' + str(block) + '.txt', 'w') as f:
		for i in res:
			f.write(str(i)+'\n')
