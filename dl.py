import os

# Ex: http://imgs.xkcd.com/clickdrag/#<n|s>#<e|w>.png
NAME_BASE = "%d%s%d%s.png"
URL_BASE = "http://imgs.xkcd.com/clickdrag/" + NAME_BASE

SAVE_LOC = os.path.join(os.getcwd(), 'images')

FINAL_IMG_LOC = os.path.join(os.getcwd(), 'final.png')

def download_image(url, folder=''):
	try:
		img = urllib2.urlopen(url)
		data = img.read()
		fname = os.path.basename(urlsplit(url)[2])

		o = open(os.path.join(
					folder,
					fname), 'wb')

		o.write(data)
		o.close()

		print 'url', url
	except:
		# probably a 404 or something
		pass

def download_all():
	import urllib2
	from urlparse import urlsplit
	
	# Basis for bounds: https://thoughtstreams.io/jtauber/xkcd-click-and-drag/
	for ns in ['n', 's']:
		for ew in ['e', 'w']:
			for ns_num in xrange(0,20):
				for ew_num in xrange(0,50):
					tup = (ns_num, ns, ew_num, ew)

					if not os.path.isfile(
						os.path.join(SAVE_LOC, NAME_BASE % tup)):

						# download only if we need to
						print '->', ns_num, ns, ew_num, ew
						dlurl = URL_BASE % tup
						download_image(dlurl, SAVE_LOC)

def join_downloaded():
	# PIL 1.1.7 http://www.pythonware.com/products/pil/
	import Image
	import re

	BASE_SIZE = 2048 # w/h for any image downloaded...
	RE_DATA = re.compile('([\d]+)([ns]{1})([\d]+)([ew]{1})', re.IGNORECASE)

	blank = Image.new("RGB", (BASE_SIZE, BASE_SIZE))

	for dirname, dirnames, filenames in os.walk(SAVE_LOC):
		for filename in filenames:
			full_path = os.path.join(dirname, filename)
			#print full_path

			# Extract position data from file name
			m = RE_DATA.findall(filename)[0]
			ns_num = m[0]
			ns = m[1]
			ew_num = m[2]
			ew = m[3]

			pos_x = BASE_SIZE * int(ew_num)
			if ew == 'w': 
				pos_x *= -1

			pos_y = BASE_SIZE * int(ns_num)
			if ns == 's': 
				pos_y *= -1

			print filename, '|', ns_num, ns, ew_num, ew, 'pos:', pos_x, pos_y

			img = Image.open(full_path)

			blank.paste(img, (pos_x, pos_y, pos_x + BASE_SIZE, pos_y + BASE_SIZE))

	blank.save(FINAL_IMG_LOC)

if __name__ == '__main__':
	#download_all()
	#join_downloaded()