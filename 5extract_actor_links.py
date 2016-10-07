# -*- coding: utf-8 -*-

import urllib
import time
import copy
import csv
import time

testfile = urllib.URLopener()

with open('actors.csv', 'rb') as f:
    reader = csv.reader(f)
    actors0 = map(list, reader)
actors = copy.deepcopy(actors0)

actors_table = open("actors_gender.csv", "w")
tag = '<a href="#actor" >'
end_tag = '</a>'
testfile = urllib.URLopener()

errors = open("actor_errors.csv", "w")

counter = 0
for a in actors[10000:10016]:
	actor = a[0]
	try:
		filename = "actor" + actor
		link = 'http://www.kinopoisk.ru/name/' + actor + '/'
		print link
		testfile.retrieve(link, filename)
	except IOError:
		print "ERROR"
		errors.write(str(actor) +","+str(link)+"\n")
	time.sleep(1)

	
	print str(counter)
	#print code
	counter+=1

f.close()
errors.close()
actors_table.close()
