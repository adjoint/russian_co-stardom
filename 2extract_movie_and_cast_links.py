# -*- coding: utf-8 -*-


beginning_tag = '<div class="name"><a href="'

ml = open("movie_links.csv", "w")
cl = open("cast_links_and_codes.csv", "w")
for i in range(1,148):
	filename = "page" + str(i)
	file = open(filename, "r")
	data = file.read()
	newdata = data.split(beginning_tag)[1:]
	for n in newdata:
		link = n.split('"')[0]
		number = link.split("/")[-2]
		ml.write("https://www.kinopoisk.ru/film/" + str(number) + "/\n")
		cl.write(str(number) + ",https://www.kinopoisk.ru/film/" + str(number) + "/cast/\n")
		print number

ml.close()
cl.close()