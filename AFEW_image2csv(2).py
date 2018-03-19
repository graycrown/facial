# /usr/bin/python
# coding : utf-8

# import sys
# import pdb
import os,shutil
import cv2
import json
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

# parameters for loading data and images
# image_path = sys.argv[1]

# EmotionName = ('neutral','anger', 'contempt','disgust', 'fear', 'happy', 'sad', 'surprise' )

np.set_printoptions(threshold='nan') # set the numpy.array print whole data but not ...
print_processInfo_switch = 0     # 0:open  1:close
single_set_draw_switch = 1  # 0:open  1:close
# result = []

def dir_data_file(data_path):
	fileList = []
	for perFile in os.listdir(data_path):
		if os.path.splitext(perFile)[1] == '.png':    # choose the fixed-kind file   .png
			fileList.append(data_path +'/'+ perFile)
	fileList.sort()
	return fileList


def dir_data_folder(data_path):
	folders = []
	for perFile in os.listdir(data_path):
		if os.path.isdir(data_path + perFile):   # only choose the folder , ignore the file 
			folders.append(data_path + perFile)
	folders.sort()
	return folders
	
detection_model_path = './trained_models/detection_models/haarcascade_frontalface_default.xml'
emotion_offsets = (0, 0)

# emotion_model_path = '../trained_models/emotion_models/fer2013_mini_XCEPTION.102-0.66.hdf5'
# gender_model_path = '../trained_models/gender_models/simple_CNN.81-0.96.hdf5'
# emotion_labels = get_labels('fer2013')

# target_file = '../result/predicted_' + EmotionName[emotion_kind] + '.txt'

# gender_labels = get_labels('imdb')
font = cv2.FONT_HERSHEY_SIMPLEX


# loading models
face_detection = load_detection_model(detection_model_path)

emotion_target_size = (48,48)
image_set_path = '../AFEW/01/'
selected_folder = '../Selected_AFEW/'

image_folder_path = dir_data_folder(image_set_path)     # get the singel moive set path
# print(image_folder_path)

total_count = 0
face_count = 0

for set in image_folder_path:
	
	# get label data
	label_file = set +'/' +  os.path.split(set)[1] + '.json'
	with open(label_file, 'r') as f_json:
		label_data = json.load(f_json)
	
	new_label_file_path = selected_folder + label_file.split('/')[-2]
	new_label_file_name = os.path.split(label_file)[-1]
	if not os.path.isdir(new_label_file_path):
		os.makedirs(new_label_file_path)
	
	shutil.copy(label_file,new_label_file_path + '/' + new_label_file_name)
	
	# print(label_file)
	
	image_path = dir_data_file(set)  # get the .png image
	# print(image_path)
	
	
	
	f = open('AFEW.csv','a')

	for num in range(len(image_path)):
	
		total_count += 1
		
		# print the process info
		if print_processInfo_switch == 0:
			print('deal with the ' + image_path[num])
		
		# loading images
		rgb_image = load_image(image_path[num], grayscale=False)
		bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
		
		gray_image = load_image(image_path[num], grayscale=True)
		
		gray_image = np.squeeze(gray_image)
		gray_image = gray_image.astype('uint8')
		# pdb.set_trace()
		
		faces = detect_faces(face_detection, gray_image)
		
		for face_coordinates in faces:
			# x1, x2, y1, y2 = apply_offsets(face_coordinates, gender_offsets)
			# rgb_face = rgb_image[y1:y2, x1:x2]
			
			
			selected_file_name = '../Selected_AFEW/' + image_path[num].split('/')[-2] + '/' + image_path[num].split('/')[-1]
			cv2.imwrite(selected_file_name, bgr_image)
			
			face_count += 1
			
			x1, x2, y1, y2 = apply_offsets(face_coordinates, emotion_offsets)
			gray_face = gray_image[y1:y2, x1:x2]

			try:
				gray_face = cv2.resize(gray_face, (emotion_target_size))
			except:
				continue
			
			
			
			# get label index
			filename = image_path[num].split('/')[-1]
			label_index = filename.split('.')[0]
			arousal = label_data['frames'][label_index]['arousal']
			valence = label_data['frames'][label_index]['valence']
			print(label_index + ' : V '+ str(valence) +' A ' + str(arousal))

			
			'''
			# write the scale file
			filename = image_path[num].split('/')[-1]
			newname = './adjustpic_neutral/'+ filename
			cv2.imwrite(newname, gray_face)
			'''
			# generate the array
			array = gray_face.reshape(48*48)
			# print(type(array))
			# read label
			'''
			label_file_name = filename.split('.')[0] + '_emotion.txt'
			flabel = open(label_folder_path+label_file_name,'r')
			label = int(float( flabel.readline()[:-1] ))
			flabel.close()
			'''
			# write to csv file
			image_data = array.tolist()
			string_data = str(image_data)[1:-1]
			string_data = string_data.replace(',','')
			f.write(str(valence)+ ',' + str(arousal) + ',' + string_data + ',' + 'Training\n')

	f.close()  # write the data in every loop
print(total_count)
print(face_count)

f = open('countfile_AFEW_01.txt','w+')
f.write('face_count : ' + str(face_count) + '\n')
f.write('total_count : ' + str(total_count) + '\n')
f.close()			
