import sys,os, cStringIO, urllib2, Image

def parseNum(url, x, y):
#	x = 57
#	y = 13
#	url = 'http://s0.meituan.net/www/css/si/pricesp/12/9fa005ea6e.va8b83670.png'
	img = Image.open(cStringIO.StringIO(urllib2.urlopen(url).read()))

	cg = img.crop((x, y + 2, x + 7, y + 12)).resize((20,30)).convert('L')
	diffs = [0,0,0,0,0,0,0,0,0,0,0]

	for yi in range(30):
		for xi in range(20):
			imgDir = os.path.join(sys.path[0],'number')
			for i in os.listdir(imgDir):
				if os.path.isfile(os.path.join(imgDir,i)) and i.endswith('.png') :
					img_i = Image.open(os.path.join(imgDir,i))
					#index = i.split('.')[0]
					if cg.getpixel((xi, yi)) != img_i.getpixel((xi, yi)):
						diffs[int(i.split('.')[0])] += 1


	return diffs.index(min(diffs))