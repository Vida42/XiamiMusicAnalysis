

#把文件切成前10块（range(1,11)是从1到10），分别存储
#0到3，是读了1到3行
for block in range(1,25):
	first=[] 
	with open('info_user.txt','r',encoding = 'utf-8') as f0:
	    g = f0.readlines()[25000*(block-1):25000*block]
	    for i in g:
	        i = i.strip('\n')
	        first.append(i)
	# print(first)

	#把列表内的内容写入文件（2\n4\n6\n……]形式）
	with open('info_user' + str(block) + '.txt', 'w',encoding = 'utf-8') as f2:
		for i in first:
			f2.write(str(i)+'\n')



# # 将R2合并至Ra
# extract = []
# for a in range(1,13):#生成2，3，4
# 	print(a)
# 	with open('genre'+ str(a) + '.txt','r',encoding = 'utf-8') as f2:
# 	        for eachline in f2:
# 	            extract.append(eachline.strip())

# with open ("genre.txt", 'a',encoding = 'utf-8') as dele_w:
# 	for i in extract:
# 		dele_w.write(str(i)+'\n')