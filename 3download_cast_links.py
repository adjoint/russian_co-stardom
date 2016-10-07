# -*- coding: utf-8 -*-

import urllib
import time
import copy
import csv
import os.path

testfile = urllib.URLopener()

with open('cast_links_and_codes.csv', 'rb') as f:
    reader = csv.reader(f)
    links0 = map(list, reader)
links = copy.deepcopy(links0)

errors = open("cast_errors.csv", "w")

counter = 0
for l in links:
	code = l[0]
	link = l[1]
	filename = "movie" + str(code)
	if not os.path.exists(filename):
		try:
			testfile.retrieve(link, filename)
			time.sleep(1)
		except IOError:
			print "ERROR"
			errors.write(str(code) +","+str(link)+"\n")
	print str(counter)
	counter+=1
f.close()
errors.close()