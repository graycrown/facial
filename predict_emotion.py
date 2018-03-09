from image_emotion_gender_demo import predict

import sys
import os

EmotionName = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprised', 'neutral')


def dir_data_folder(data_path):
	folders = []
	for perFile in os.listdir(data_path):
		if os.path.isdir(data_path + perFile):   # only choose the folder , ignore the file 
			folders.append(data_path + perFile + '/')
	folders.sort()
	return folders


def predict_all(image_folder_path):
	
	result = []
	
	for count in range(len(image_folder_path)):
		singel_result = predict(image_folder_path[count],count)
		result.append(singel_result)

	true_pre = 0
	total = 0
	face_cnt = 0
	#  [true_cnt,total_cnt,face_cnt,total_accuracy,face_recog_ratio,recog_accuracy]
	for cnt in result:
		true_pre += cnt[0]
		total += cnt[1]
		face_cnt += cnt[2]
		
	total_accuracy = true_pre / float(total)
	face_accuracy = face_cnt / float(total)
	recog_accuracy_in_face = true_pre / float(face_cnt)
	
	f = open('../result/total.txt','w+')
	for l in range(len(result)):
		f.write(EmotionName[l] + ' : ')
		for tmp in result[l]:
			f.write(str(tmp) + '  ')
		f.write('\n')

	f.write('total accuracy = ' +  str(total_accuracy) + '\n')
	f.write('face recognize accuracy = ' +  str(face_accuracy)+ '\n')
	f.write('predicted accuracy in recognized face = ' +  str(recog_accuracy_in_face)+ '\n')
	f.close()

	
def predict_one(image_folder_path,count):
	predict(image_folder_path,count)	



num = 0
while num != 1 and num != 2 and num != 3:
	num = input('select a dataset:\n   0.qiut\n   1.fer2013\n   2.fer2013_simple\n   3.CK2_sample\n  ')
	num = int(num)
	if num == 1 :
		dateset_path = '../datasets/FER2013/'      # fer2013 database path
	elif num == 2:
		dateset_path = '../datasets/Success/'      # fer2013_sample database path
	elif num == 3:
		dateset_path = '../datasets/CK2_sample/'      # CK2 database path
	elif num == 0:
		os._exit(0)
	else:
		print('unexpected input ,select again!\n')	
	
image_folder_path = dir_data_folder(dateset_path)

num = 0
while num != 1 and num != 2:
	num = input('choose the item you need: \n  0.quit \n  1.predict all dataset \n  2.predict one EmotionSet \n')
	num = int(num)
	if num == 1:
		predict_all(image_folder_path)
	elif num == 2:
		setnum = input("input the num to choose a set : {0:'angry',1:'disgust',2:'fear',3:'happy',4:'sad',5:'surprise',6:'neutral'} \n")
		setnum = int(setnum)
		predict_one(image_folder_path[setnum],setnum)
	elif num == 0:
		os._exit(0)
	else :
		print('unexpected num,please choose again')

