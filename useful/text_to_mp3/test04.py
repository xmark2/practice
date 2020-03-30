from gtts import gTTS
import os
import glob
from pathlib import Path

def readfile(file):
	with open(file, encoding="utf-8") as f:
		data = f.read()
		return data

def list_files(path,file_type):
	# path = './input'
	# files = [f for f in glob.glob(path + "**/*."+file_type, recursive=True)]
	files = glob.glob(path + "/**/*."+file_type, recursive=True)
	
	# for subpath in subpaths:
	# 	subfiles = [f for f in glob.glob(subpath + "**/*."+file_type, recursive=True)]
	# 	# files = files +subfiles
	# 	print(subfiles)
	return files


# def list_files2(path,file_type):
# 	for file_type in Path(path).rglob('*'):
#     	print(file_type)

def textmp3(file):
	print(file)
	try:
		mytext = readfile(file)
		# print(mytext)
		tts = gTTS(text=mytext, lang='hu')
		filename = file.replace('txt','mp3')
		print(filename+" saved")
		tts.save(filename)
	except:
		pass
	# os.system(filename+"mpg321.mp3")


def main():
	# print(list_files('txt'))
	print(list_files('./input','txt'))
	# subpaths = os.listdir('./input')
	# subpaths = ['./input/'+x for x in subpaths]

	# filesNew = []
	# for subpath in subpaths:
	# 	filesNew.extend(list_files(subpath,'txt'))

	files = list_files('./input','txt')

	for file in files:
		# print(file)
		textmp3(file)	

	# print(subpaths)
	# textmp3('szoveg1.txt')

if __name__ == '__main__':
	main()
	# print('hello')