from gtts import gTTS
import os

def readfile(file):
	with open(file, encoding="utf-8") as f:
		data = f.read()
		return data

def textmp3(file):
	mytext = readfile(file)
	# print(mytext)
	tts = gTTS(text=mytext, lang='hu')
	filename = file.replace('txt','')
	tts.save(filename+".mp3")
	# os.system(filename+"mpg321.mp3")

def main():
	textmp3('szoveg1.txt')

if __name__ == '__main__':
	main()