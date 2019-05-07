from bs4 import BeautifulSoup
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

import pandas

def preprocess(soup):
	btry = list()
	spec=list()
	for box in soup.find_all('div', attrs={'class':'_1-2Iqu row'}):
		name.append(box.find('div', attrs={'class':'_3wU53n'}).get_text().encode("UTF-8"))
		rating.append(box.find('div', attrs={'class':'hGSR34'}).get_text().encode("UTF-8"))
		specs =  box.find_all('li', attrs={'class':'tVe95H'})
		spec.append(specs[0].get_text().encode("UTF-8"))
		btry.append(specs[3].get_text().encode("UTF-8"))
		price.append(box.find('div', attrs={'class':'_1vC4OE _2rQ-NK'}).get_text().encode("UTF-8")[3:].replace(",",""))

	for i in spec:
		x = i.split('|')
		ram.append(x[0][:x[0].find(' ')])
		x[1] = x[1][1:]
		internal.append(x[1][:x[1].find(' ')])

	for i in btry:
		battery.append(i[:i.find(' ')])

name=list()
price=list()
rating=list()
battery = list()
ram=list()
internal=list()
no_of_pages = 5

for i in range(no_of_pages):
	quote_page = 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.rating%255B%255D%3D1%25E2%2598%2585%2B%2526%2Babove&otracker=categorytree&sort=price_asc&p%5B%5D=facets.price_range.from%3D10000&p%5B%5D=facets.price_range.to%3DMax&p%5B%5D=facets.operating_system%255B%255D%3DAndroid&p%5B%5D=facets.serviceability%5B%5D%3Dfalse&page='+str(i+1)
	print quote_page
	page = urlopen(quote_page)
	soup = BeautifulSoup(page, 'html.parser')
	preprocess(soup)

df = pandas.DataFrame(data={ "name":name,"ram": ram,"internal":internal,"price": price,"rating":rating,"battery":battery})
df.to_csv("./1.csv", sep=',',index=False)
