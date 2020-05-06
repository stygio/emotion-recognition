import os
import pandas as pd
from tqdm import tqdm

drive_path = 'drive/My Drive/aff_wild/'
drive_images_path = os.path.join(drive_path, 'images')

dataset_path = 'D:/aff_wild'
images_path = os.path.join(dataset_path, 'images')
valence_path = os.path.join(dataset_path, 'annotations', 'train', 'valence')
arousal_path = os.path.join(dataset_path, 'annotations', 'train', 'arousal')
filenames = []
valence = []
arousal = []

# For each folder of frames from a video
for video_name in os.listdir(images_path):
	folder_path = os.path.join(images_path, video_name)
	valence_file = open(os.path.join(valence_path, video_name) + '.txt', 'r')
	arousal_file = open(os.path.join(arousal_path, video_name) + '.txt', 'r')
	file_line_cursor = 0
	# Sort the files, since python won't sort them correctly by default (i.e. it will be 0.jpg, 1.jpg, 10.jpg instead of 0.jpg, 1.jpg, 2.jpg)
	frames = sorted(os.listdir(folder_path), key = lambda f: int(os.path.splitext(f)[0]))
	# For each frame in that folder
	for f in tqdm(frames, desc = video_name):
		# Append the appropriate location of the file with the google drive prefix
		filenames.append(drive_images_path + '/' + video_name + '/' + f)
		f, _ = os.path.splitext(f)
		# Some images might not exist due to no face being detected in a frame
		# Make sure that the file line number corresponds to the actual frame
		while file_line_cursor != int(f):
			valence_file.readline()	
			arousal_file.readline()
			file_line_cursor += 1
		# Read the lines from the valence and arousal files
		line = valence_file.readline()	
		valence.append(line.strip())
		line = arousal_file.readline()
		arousal.append(line.strip())
		file_line_cursor += 1

	valence_file.close()
	arousal_file.close()

lf = len(filenames)
lv = len(valence)
la = len(arousal)
assert lf == lv and lf == la, "Incompatible lengths - filenames: {}, valence values: {}, arousal values: {}".format(lf, lv, la)

dictionary = { 'Loc' : filenames,
               'Valence' : valence,
               'Arousal' : arousal}

df = pd.DataFrame(dictionary)
df.to_csv(os.path.join(dataset_path, 'input.csv'), index = False, header = False)

