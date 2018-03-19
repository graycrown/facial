#!/usr/bin/python
#coding:utf-8

import random
import csv   
import numpy as np
import pprint as pp


total_count = len(open('AFEW.csv','rU').readlines()) - 1
print(total_count)
test_count = int(0.1 * total_count)
print(test_count)
resultList=random.sample(range(0,total_count+1),test_count)
resultList.sort()

# print(resultList)
Index = 0
count = -1
label = -1
new_file = open('new_AFEW1.csv','a')  
with open('AFEW.csv','r') as csvfile: 
	pre_reader=csv.DictReader(csvfile)#直接生成一个pre_reader，用于迭代读出 
	for reader in pre_reader:#迭代读出pre_reader里的数据  
		count += 1
		# print(count)
		valence = float(reader["valence"])
		arousal = float(reader["arousal"])
		if pow(valence,2) + pow(arousal,2) <= 4:
			label = 0
		else:
			if valence >= 0 and arousal >= 0:
				label = 1
			elif valence < 0 and arousal > 0:
				label = 2
			elif valence <= 0 and arousal <= 0:
				label = 3
			elif valence > 0 and arousal < 0:
				label = 4
		
		if count == resultList[Index]:
			if Index < test_count - 1:
				Index += 1
			new_file.write(str(label) + ',' + reader["pixels"] + ',' + 'PublicTest\n')
		else:
			new_file.write(str(label) + ',' + reader["pixels"] + ',' + reader["Usage"] + '\n')
		
new_file.close()
#        print(x)  
'''          
        arry = [int(i) for i in x ]#将x中一个个字符转化为int类型，arry是个int数组  
#        print(arry)  
#        print(type(arry[1]))  
          
        result=np.array(arry)#生成np 的array  
        result=result.reshape([48,48])#变成48*48的形状  
#        pp.pprint(result)#显示一些转化后的结果  
        image = Image.fromarray(result)#从数据，生成image对象  
        image=image.resize([384,384],Image.ANTIALIAS)#抗锯齿的放大  
          
                             
          
        plt.figure("test")#  
        plt.imshow(image)#建立窗口  
        plt.show()#显示图片  
        time.sleep(2)#延时300ms  
  
          
                             
                             
          
                      
#        image.show()#显示图片  
        os.system("pause")  
        number=reader["emotion"]#读出这张图片对应的表情标签  
    #    print(number)  
        name="/image"+str(image_number[int(number)])+".png"  
        path=os.path.join("./fer2013/",number)#生成这个表情图片对应的路径  
    #    print((path+name))  
        print("正在保存%s类型表情%s"%(number,name))  
        image_save=image.convert("L")#转化为灰度图片(这一步很关键，不然图片不能以png格式保存)  
        image_save.save(path+name)#  
        print("第%d保存成功！"%(couter_num))#显示已经保存了第几张  
        image_number[int(number)]=image_number[int(number)]+1  
        couter_num+=1  
'''
