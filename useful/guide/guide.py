import wikipedia
import folders
from pydub import AudioSegment
from pydub import effects

import sys
sys.path.append('/path/to/ffmpeg')

def write_file(file,data):
	# f = open(file, "w")
	# f.write(data)
	# f.close()
	with open(file, 'w') as f:
		f.write(data)

def getwiki(path_wiki,title):
	wikipedia.set_lang("hu")
	mycontent = wikipedia.page(title).content
	mycontent = mycontent.split('\n')
	mycontent = [x for x in mycontent if len(x)>0]
	mycontent = '\n'.join(mycontent)

	filename = title.replace("-","_").replace(":","_").replace("!","_").replace("\\","_")
	write_file(path_wiki+'/'+filename+'.txt',mycontent)

def mp3_speed(root):
	# root = r'original/abc.mp3'
	velocidad_X = 1.5 # No puede estar por debajo de 1.0

	sound = AudioSegment.from_mp3(root)
	so = sound.speedup(velocidad_X, 150, 25)
	so.export(root[:-4] + '_out.mp3', format = 'mp3')

def main(path_wiki,path_out):

	# print(mp3files)
	# folders.create_folder(path_wiki)

	# with open('list.txt','r') as f:
	# 	data = f.read()

	# titles = data.split('\n')
	# print(titles)
	# for title in titles:
	# 	getwiki(path_wiki,title)

	# folders.folder_in_out(path_wiki,path_out)
	mp3files = folders.list_files2('output', 'mp3')
	# mp3_mod = [mp3_speed(x) for x in mp3files]
	for mp3file in mp3files:
		print(mp3file)
		mp3_speed(mp3file)

if __name__ == '__main__':
	path_wiki = 'output/wiki'
	path_out = 'output/mp3/'
	main(path_wiki,path_out)


	# with open(file,'w') as f:
		# f.write(data)

# mycontent = ny.content



# file.
# u'New York is a state in the Northeastern region of the United States. New York is the 27th-most exten'...
# ny.links[0]