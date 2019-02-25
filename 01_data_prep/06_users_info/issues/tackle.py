others = []
with open('others' '.txt','r',encoding = 'utf-8') as f2:
	for eachline in f2:
		others.append(eachline.strip('\n'))

a = []

for two in others:
	a.append(two + '\t' + '虾米音乐人' + '\t' + str(0) + '\t' + str(0) + '\t' + 'Lv0' + '\t' + '0次访问' + '\t' + str(0) + '\t' + str(0) + '\t' + str(0))
print(len(a))


# li2 = []
# for much in d:
# 	k = much.replace('http://www.xiami.com','').replace('/genre/detail/gid/',',gid').lstrip(',')
# 	li2.append(k)
# # print(d)
# # print(li2)


with open('three' + '.txt', 'w',encoding = 'utf-8') as f2:
	for i in range(len(a)):
		f2.write(a[i] + '\n')
