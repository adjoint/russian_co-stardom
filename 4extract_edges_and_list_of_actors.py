# -*- coding: utf-8 -*-

import urllib
import time
import copy
import csv

beginning_tag = '<div class="name"><a href="/name/'

with open('cast_links_and_codes.csv', 'rb') as f:
    reader = csv.reader(f)
    links0 = map(list, reader)
links = copy.deepcopy(links0)

edges = open("edges.csv", "w")
actors_table = open("actors.csv", "w")
actors_array = []

counter = 0
for l in links:
	code = l[0]
	link = l[1]
	if code!="898919":
		filename = "movie" + str(code)
		movie = open(filename, "r")
		actors = []
		data = movie.read()
		if data.find('<a name="actor"></a>')!=-1:
			ndata = data.split('<a name="actor"></a>')[1]
			try:
				n2data = ndata.split('<a name="producer"></a>')[0]
			except IndexError:
				print code
			newdata = n2data.split(beginning_tag)
			for d in newdata[1:]:
				actor = d.split("/")[0]
				actors.append(actor)
			for i in range(len(actors)-1):
				for j in range(i+1, len(actors)):
					edges.write(actors[i]+","+actors[j]+"\n")
			for actor in actors:
				if actor not in actors_array:
					actors_array.append(actor)
	
		#print code
	
	print str(counter)
	#print code
	counter+=1
for actor in actors_array:
	actors_table.write(actor + "\n")
f.close()
edges.close()
actors_table.close()