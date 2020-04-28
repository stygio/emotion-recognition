import cv2
import os
from tqdm import tqdm
import numpy as np

video_folder_path = "D:/aff_wild/videos/train"
bbox_folder_path  = "D:/aff_wild/bboxes/train"
images_folder_path = "D:/aff_wild/images"


"""
Retrieves the frame at current cursor position in the video
	video_handle - cv2.VideoCapture() object for the video
"""
def getFrame(video_handle):
	success_flag, frame = video_handle.read()
	if not success_flag:
		raise Exception("cv2.VideoCapture() returned (False, _)")
	return frame


"""
Get boundingbox
	bbox_filename - absolute path to folder with boundingbox files for a certain video
	frame_nr	  - which frame from the video
"""
def get_bbox(bbox_filename, frame_nr):
	l, r, t, b = None, None, None, None
	with open(bbox_filename, 'r') as f:
		for i, line in enumerate(f):
			line = line.replace('\n', '')
			if i == 3:
				l = int(float(line.split(' ')[0]))
				t = int(float(line.split(' ')[1]))
			if i == 4:
				b = int(float(line.split(' ')[1]))
			if i == 5:
				r = int(float(line.split(' ')[0]))

	return (t, b, l, r)


"""
Crop the passed image according to boundingbox information
	img - an image in the form of a numpy array
	box - boundingbox in the form of (top, bottom, left, right)
"""
def crop_image(img, box):
	top, bottom, left, right = box
	(img_height, img_width, _) = np.shape(img)
	cropped_img = img[max(top, 0):min(bottom, img_height-1), max(left, 0):min(right, img_width-1)]

	return cropped_img


"""
Extracts faces from the requested video
	video_name - video to extract faces from
"""
def extract_faces_from_video(video_name):
	# Open the video & determine its length
	video_path = os.path.join(video_folder_path, video_name)
	video_handle = cv2.VideoCapture(video_path)
	assert video_handle.isOpened(), "Unable to open " + video_name
	video_length = video_handle.get(7)
	# Create a folder for the extracted faces
	faces_folder = video_name.partition(".")[0] + "/"
	faces_folder = os.path.join(images_folder_path, faces_folder)
	os.makedirs(faces_folder, exist_ok = True)

	# The folder of bbox files for this video
	video_bbox_folder = os.path.join(bbox_folder_path, os.path.splitext(video_name)[0])
	# Main face extraction loop
	for frame_nr in tqdm(range(int(video_length)), desc = 'Extracting from ' + video_name):
		# Check that a boundingbox exists for this frame
		frame = getFrame(video_handle)
		bbox_filename = os.path.join(video_bbox_folder, str(frame_nr)) + ".pts"
		if os.path.isfile(bbox_filename):
			# Get the frame
			face = crop_image(frame, get_bbox(bbox_filename, frame_nr))
			image_filename = os.path.join(faces_folder, "{0}.jpg".format(frame_nr))
			cv2.imwrite(image_filename, face)


videos = os.listdir(video_folder_path)
for video in videos[1:5]:
	extract_faces_from_video(video)

