from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import pprint
pp = pprint.PrettyPrinter(indent=4)

def main(): # Main function
	current_year = int(datetime.datetime.now().year)
	url = "http://www.imdb.com/search/title?release_date=" + str(current_year) + "," + str(current_year) + "&title_type=feature"
	html = urlopen(url)
	soup = BeautifulSoup(html.read(), features="html.parser")
	dataset_top50 = {}
	id = 1
	movies_list = soup.findAll('div', attrs={'class': 'lister-item-content'})
	for each in movies_list:

		# Prototype of each movie item
		movie_item = {
			'name': '',
			'certificate': '',
			'runtime': '',
			'genre': '',
			'description': '',
			'director': '',
			'stars': [],
			'votes': '',
			'gross': ''
		}

		if each.find('h3', attrs={'class': 'lister-item-header'}).find('a').text:
			name_value = each.find('h3', attrs={'class': 'lister-item-header'}).find('a').text
			movie_item['name'] = name_value

		dataset_top50[id] = movie_item
		id += 1

	pp.pprint(dataset_top50)

	# End of the main function


main() # Call of the main function