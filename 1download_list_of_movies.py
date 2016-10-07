import urllib
import time

testfile = urllib.URLopener()

for i in range(1,148):
	link = "https://www.kinopoisk.ru/lists/ord/name/m_act%5Bcountry%5D/2/m_act%5Ball%5D/ok/page/" + str(i) + "/"
	filename = "page" + str(i)


	testfile.retrieve(link, filename)
	time.sleep(1)
	print str(i)
	time.sleep(1)

