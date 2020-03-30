with open('youtube.txt') as file:
	toplist = file.read().split('\n')



f = open("youtube2.txt", "a")
# for topsong in toplist[:5]:
for topsong in toplist:
	topsong = 'youtube2mp3 -d ~/Desktop/youtube_mp3/mp3 -y '+topsong
		
	
	f.write(topsong+'\n')
	print(topsong)