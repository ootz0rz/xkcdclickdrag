# Ex: http://imgs.xkcd.com/clickdrag/#<n|s>#<e|w>.png
URL_BASE = "http://imgs.xkcd.com/clickdrag/%d%s%d%s.png"

def download_image(url, folder='images'):
	import urllib2
	import os
	from urlparse import urlsplit

	try:
		img = urllib2.urlopen(url)
		data = img.read()
		fname = os.path.basename(urlsplit(url)[2])

		#print 'fname', fname
		# print 'data', data

		o = open(os.path.join(
					os.path.join(os.getcwd(), folder),
					fname), 'wb')

		o.write(data)
		o.close()

		print 'url', url
	except:
		pass

if __name__ == '__main__':
	# Bounds: https://thoughtstreams.io/jtauber/xkcd-click-and-drag/
	for ns in ['n', 's']:
		for ew in ['e', 'w']:
			for ns_num in xrange(0,20):
				for ew_num in xrange(0,50):
					print '->', ns_num, ns, ew_num, ew
					dlurl = URL_BASE % (ns_num, ns, ew_num, ew)
					download_image(dlurl)