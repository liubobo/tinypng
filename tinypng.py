import tinify
import os 
tinify.key = 'cRIu54yRk8ubjhkNK4a3-DdKNUKHJdTm'

for root, dirs, files in os.walk("./guide_pic", topdown=False):
	for file  in files:
		  if file.endswith('png'):
		  	  print file
			  print tinify.from_file(root+'/' + file).to_file(root+'/' + file)

