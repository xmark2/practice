import wikipedia
import folders

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


def main(path_wiki,path_out):
	folders.create_folder(path_wiki)

	with open('list.txt','r') as f:
		data = f.read()

	titles = data.split('\n')
	print(titles)
	for title in titles:
		getwiki(path_wiki,title)

	folders.folder_in_out(path_wiki,path_out)

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