
with open('toplist.txt') as file:
	toplist = file.read().split('\n')

print(toplist[2])


from googlesearch import search
# for url in search('"Breaking Code" WordPress blog', stop=20):

# data = []
f = open("youtube.txt", "a")
# for topsong in toplist[:5]:
for topsong in toplist:
	print(topsong)
	for url in search(topsong, stop=3):
		# data = data.append(url)
		# youtube = list(filter(lambda x: 'youtube' in url, url))
		if 'youtube' in url:
			f.write(url+'\n')
			print(url)
			break


f.close()