# import sys
# import pdb
import os
import cv2
from keras.models import load_model
import numpy as np

# from utils.datasets import get_labels
from utils.inference import detect_faces
from utils.inference import draw_text
from utils.inference import draw_bounding_box
from utils.inference import apply_offsets
from utils.inference import load_detection_model
from utils.inference import load_image
from utils.preprocessor import preprocess_input

np.set_printoptions(threshold='nan') # set the numpy.array print whole data but not ...
print_processInfo_switch = 0     # 0:open  1:close
single_set_draw_switch = 1  # 0:open  1:close
result = []

def dir_data_folder(data_path):
	folders = []
	for perFile in os.listdir(data_path):
		folders.append(data_path + perFile)
		folders.sort()
	return folders


font = cv2.FONT_HERSHEY_SIMPLEX


emotion_target_size = (48,48)
image_folder_path = './CK/Emotion image/'
label_folder_path = './CK/Labels/'
image_path = dir_data_folder(image_folder_path)


count = 0


for num in range(len(image_path)):
	# print the process info
	if print_processInfo_switch == 0:
		print('deal with the ' +  image_path[num])
	
	# loading images
	
	
	filename = image_path[num].split('/')[-1]
	label_file_name = filename.split('.')[0] + '_emotion.txt'
	flabel = open(label_folder_path+label_file_name,'r')
	label = int(float( flabel.readline()[:-1] ))
	flabel.close()
	
	number = str(label)
	
	#print(number)
	# name="/image"+str(image_number[int(number)])+".png"  
	path=os.path.join("./CK_classify/",number)#
	if not os.path.exists(path):
		os.makedirs(path)

	newname = path+ '/' + filename
	print(newname)
	cv2.imwrite(newname, rgb_image)
	
	count += 1


print(count)

