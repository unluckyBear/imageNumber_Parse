import os, cStringIO, urllib2, Image
from imgParse import parseNum

x = 28
y = 26
url = 'http://s0.meituan.net/www/css/si/pricesp/12/365d7c44e7.ve37b1e42.png'
print parseNum(url, x, y)
#print str(3) + (str(8))
#img = Image.open(cStringIO.StringIO(urllib2.urlopen(url).read()))
#img.crop((x, y + 2, x + 7, y + 12)).resize((20,30)).save('3.png')