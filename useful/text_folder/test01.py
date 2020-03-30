import os
import glob

def create_folder(path):
	# path = './dail/first/second/third'
	os.makedirs(path, exist_ok=True)

def write_file(file,data):
	f = open(file, "w")
	f.write(data)
	f.close()

def readfile(file):
	with open(file, encoding="utf-8") as f:
		data = f.read()
		return data

def list_files(file_type):
	path = './input_files'

	files = [f for f in glob.glob(path + "**/*."+file_type, recursive=True)]
	return files
	# for f in files:
    	# print(f)

files = list_files('txt')


folders = [x.split('/')[-1].replace('.txt','') for x in files]
folders = ['./output/'+x for x in folders]
folders_a = [create_folder(x) for x in folders]

# print(folders)
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

	path = file.replace('input_files','output').replace('.txt','')

	# write_file(path+'/'+output[0][0]+'.txt',output[0][1])
	for elem in output:
		write_file(path+'/'+elem[0][:20]+'.txt',elem[1])

	# break