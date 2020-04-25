from gtts import gTTS
import os
import glob
from pathlib import Path

import os
import glob

def create_folder(path):
	# path = './dail/first/second/third'
	os.makedirs(path, exist_ok=True)

def write_file(file,data):
	with open(file, 'w') as f:
		f.write(data)

def readfile(file):
	with open(file, encoding="utf-8") as f:
		data = f.read()
		return data

def list_files(path, file_type):
	

	files = [f for f in glob.glob(path + "**/*."+file_type, recursive=True)]
	return files
	# for f in files:
    	# print(f)
# path_wiki = 'output/wiki'

# files = list_files(path_wiki,'txt')

# path_out = 'output/mp3/'

def textmp3(file, text):
	try:
		tts = gTTS(text=text, lang='hu')
		print(file +" saved")
		tts.save(file+'.mp3')
	except:
		pass

def folder_in_out(path_wiki,path_out):

	files = list_files(path_wiki,'txt')

	# print(files)
	folders = [x.split('/')[-1].replace('.txt','') for x in files]
	folders = [path_out+x for x in folders]
	folders_a = [create_folder(x) for x in folders]

	# # print(folders)
	for file in files:
		print(file)

		content_full = readfile(file)	
		content = content_full.split('\n')
		mp3_files = [x.replace('=','_') for x in content if '=' in x]

		c = 0
		mp3_files = [str(c)+x for c,x in enumerate(mp3_files,100)]

		# print(mp3_files)
		
		# content = [x.replace('=','_') for x in content if '=' in x else x]
		contentNew = []
		for row in content:

			if '=' in row:
				contentNew.append('@')
			else:
				contentNew.append(row)

		# contentNew.insert(0,'@')
		content = '\n'.join(contentNew).split('@')
		content = content[1:]
		
		print(len(mp3_files))
		print(len(content))
		# print(content[2])
		output = list(zip(mp3_files,content))
		# print(output[0])

		path = file.replace(path_wiki,path_out).replace('.txt','')

		# write_file(path+'/'+output[0][0]+'.txt',output[0][1])
		for elem in output:
			file = path+'/'+elem[0][:20]
			text = elem[1]
			if len(text.replace('\n',''))>0:
				textmp3(file, text)
				write_file(file+'.txt',text)

		# break

# if __name__ == '__main__':
	# pass		
	# path_wiki = 'output/wiki'
	# path_out = 'output/mp3/'
	# folder_in_out(path_wiki,path_out)