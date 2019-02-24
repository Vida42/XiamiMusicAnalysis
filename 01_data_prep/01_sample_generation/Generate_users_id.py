# _*_ coding:utf-8 _*_ 


# 325000000

#均匀随机抽取3万2千5百名用户，存于Xu1
import random  
import numpy

lower_limit = 1
upper_limit = 325000000
a = lower_limit
b = upper_limit


# 在a到b2范围，生成32500个数，整数，经作图发现是均匀分布
res = [random.randint(a, b) for _ in range(1, 32501)]


#把列表内的内容写入文件（2\n4\n6\n……]形式）
with open('Xu1.txt', 'w') as fl:
  for i in res:
      fl.write(str(i)+'\n')