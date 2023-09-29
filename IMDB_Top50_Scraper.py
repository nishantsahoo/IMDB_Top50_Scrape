import os
import sys
import datetime
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

dataset_location = os.path.join(os.path.dirname(__file__), "DataSets")

if not os.path.exists(dataset_location):
    os.makedirs(dataset_location)

current_year = datetime.datetime.now().year

headers = {'User-agent': 'Mozilla/5.0'}

try:
    input_year = int(input("Please enter the start year (e.g., 2016): "))
except ValueError:
    print("Invalid input. Please enter a valid year.")
    sys.exit(1)

if input_year > current_year:
    print("No movies are recorded in the year %i yet!" % input_year)
    sys.exit(1)

for year in tqdm(range(input_year, current_year + 1)):

    output_file_path = os.path.join(dataset_location, f"IMDB_Top50_{year}.txt")
    
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        url = f"http://www.imdb.com/search/title?release_date={year},{year}&title_type=feature"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        article = soup.find('div', attrs={'class': 'article'}).find('h1')
        output_file.write(article.contents[0] + ':\n')

        movieList = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})
        for i, div_item in enumerate(tqdm(movieList, desc=f"Year {year}", ncols=100)):
            div = div_item.find('div', attrs={'class': 'lister-item-content'})
            header = div.findChildren('h3', attrs={'class': 'lister-item-header'})
            movie_title = header[0].findChildren('a')[0].text
            output_file.write(f"{i + 1}. Movie: {movie_title}\n")
