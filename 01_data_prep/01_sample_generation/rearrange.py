

# for a in range(9,13):#生成6，7，8
# 	print(a)
# 将figure31,figure32,figure33,figure34放一起写入figure4
# extract = []
# for a in range(1,5):#生成1，2，3，4
# 	with open('figure3'+ str(a) + '.txt','r') as f2:
# 	        for eachline in f2:
# 	            extract.append(eachline.strip())
# print(extract)
# with open ("figure4.txt", 'a') as dele_w:
# 	for i in extract:
# 		dele_w.write(str(i)+'\n')


# ========以上为测试========


# 重排X2至X3
# extract = []
# for a in range(97,101):#生成97，98，99，100
# 	print(a)
# 	with open('Xu2_'+ str(a) + '.txt','r') as f2:
# 	        for eachline in f2:
# 	            extract.append(eachline.strip())

# with open ("X3_47.txt", 'a') as dele_w:
# 	for i in extract:
# 		dele_w.write(str(i)+'\n')


# 重排X3至X4
extract = []
for a in range(4,6):#生成1，2，3，4
	print(a)
	with open('X3_4'+ str(a) + '.txt','r') as f2:
	        for eachline in f2:
	            extract.append(eachline.strip())

with open ("X4_4b.txt", 'a') as dele_w:
	for i in extract:
		dele_w.write(str(i)+'\n')