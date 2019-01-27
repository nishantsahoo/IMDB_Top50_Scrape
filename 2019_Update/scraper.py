from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime

def main(): # Main function
	current_year = int(datetime.datetime.now().year)
	url = "http://www.imdb.com/search/title?release_date=" + str(current_year) + "," + str(current_year) + "&title_type=feature"
	html = urlopen(url)
	soup = BeautifulSoup(html.read(), features="html.parser")
	print(soup)


main() # Call of the main function