from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime

def main(): # Main function
	current_year = int(datetime.datetime.now().year)
	url = "http://www.imdb.com/search/title?release_date=" + str(current_year) + "," + str(current_year) + "&title_type=feature"
	html = urlopen(url)
	soup = BeautifulSoup(html.read(), features="html.parser")
	dataset_top50 = []
	movies_list = soup.findAll('div', attrs={'class': 'lister-item-content'})
	for each in movies_list:
		print(each)
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


	# End of the main function


main() # Call of the main function