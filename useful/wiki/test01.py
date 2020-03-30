import wikipedia

def write_file(file,data):
	f = open(file, "w")
	f.write(data)
	f.close()

def mywiki(title):
	wikipedia.set_lang("hu")
	mycontent = wikipedia.page(title).content
	mycontent = mycontent.split('\n')
	mycontent = [x for x in mycontent if len(x)>0]
	mycontent = '\n'.join(mycontent)

	filename = title.replace("-","_").replace(":","_").replace("!","_").replace("\\","_")
	write_file(filename+'.txt',mycontent)
# wikipedia.summary("Facebook", sentences=1)

titles = ["Róma","Vatikán","római pápa","Szent Péter-bazilika","Colosseum","Forum Romanum",
			"Trevi-kút","Pantheon (Róma)","Piazza Navona","Angyalvár","Capitolinus",
			"Sixtus-kápolna","A Sixtus-kápolna mennyezetfreskója","Vatikáni Múzeum"]

def main(titles):
	for title in titles:
		mywiki(title)

if __name__ == '__main__':
	main(titles)


	# with open(file,'w') as f:
		# f.write(data)

# mycontent = ny.content



# file.
# u'New York is a state in the Northeastern region of the United States. New York is the 27th-most exten'...
# ny.links[0]