# pip install  tinify

import tinify
import os,sys
tinify.key = 'cRIu54yRk8ubjhkNK4a3-DdKNUKHJdTm'
pic_path =  sys.argv[1]

for root, dirs, files in os.walk(pic_path, topdown=False):
	for file  in files:
		  if file.endswith('png'):
		  	  print file
			  tinify.from_file(root+'/' + file).to_file(root+'/' + file)

print '--------finish--------'

