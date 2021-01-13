import sys
import os
from PIL import Image

#from sys grab first and 2nd argument
#check if new exist, if not, create #use os or pathlib
#loop through pokedex folder then convert to png 
#save to new folder

jpg_folder = sys.argv[1]
png_folder = sys.argv[2]

if not os.path.exists(png_folder):
	os.makedirs(png_folder)

for filename in os.listdir(jpg_folder):
	if filename.endswith(".jpg"):
		prefix = filename.split(".jpg")[0]
		img_path = os.path.join(png_folder, (prefix + '.png'))
		im = Image.open(os.path.join(jpg_folder, filename))
		im.convert("RGB").save(img_path, 'png')
		continue
	else:
		continue

