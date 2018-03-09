import os
import sys
from PIL import Image


fold_path = './screen_happy/'   # source image folder path

export_folder_path = './HappyFixed/'    # target fold path

label_data = 'happy_label.txt'      # label data


def dir_data_folder(data_path):
    folders = []
    for perFile in os.listdir(data_path):
        folders.append(perFile)
    return folders
	

	
	
if __name__ == '__main__':
	
	imFiles = dir_data_folder(fold_path)
	imFiles.sort()

	label = []
	
	for l in open(label_data):
		row = [int(x) for x in l.split()]
		if len(row) > 0:
			label.append(row)

	count = 0

	for imNum in range(len(imFiles)):
	
		imFileName = imFiles[imNum]
		
		count = label.index([1],count) +1
		
		img_id = str(count).zfill(4)

		NewName = export_folder_path + 'image_' + img_id + '.jpg'
		# NewName = export_folder_path + imFileName
		im = Image.open(fold_path + imFileName)
		out = im.resize((1280,720), Image.ANTIALIAS)  
		out.save(NewName, quality=100)
		# count += 1
