# #把文件切成前10块（range(1,11)是从1到10），分别存储
# #0到3，是读了1到3行
# for block in range(1,12):
# 	first=[] 
# 	with open('info_music.txt','r',encoding = 'utf-8') as f0:
# 	    g = f0.readlines()[70000*(block-1):70000*block]
# 	    for i in g:
# 	        i = i.strip('\n')
# 	        first.append(i)
# 	# print(first)

# 	#把列表内的内容写入文件（2\n4\n6\n……]形式）
# 	with open('info_music' + str(block) + '.txt', 'w',encoding = 'utf-8') as f2:
# 		for i in first:
# 			f2.write(str(i)+'\n')


# 将album_x合并至Ra
extract = []
for a in range(4,15):#生成2，3，4
    print(a)
    with open('album'+ str(a) + '.txt','r',encoding="UTF-8") as f2:
            for eachline in f2:
                extract.append(eachline.strip())

with open ("Rc.txt", 'a',encoding="UTF-8") as dele_w:
    for i in extract:
        dele_w.write(str(i)+'\n')