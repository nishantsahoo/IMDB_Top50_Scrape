from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime

def main(): # Main function
	current_year = int(datetime.datetime.now().year)
	url = "http://www.imdb.com/search/title?release_date=" + str(current_year) + "," + str(current_year) + "&title_type=feature"
	html = urlopen(url)
	soup = BeautifulSoup(html.read(), features="html.parser")
	dataset_top50 = {}
	movies_list = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})
	print(movies_list)

	# End of the main function


main() # Call of the main function