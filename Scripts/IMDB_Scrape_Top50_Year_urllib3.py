import requests
import sys
from bs4 import BeautifulSoup
from tqdm import tqdm

name = input('Enter your name: ')
year = str(int(input('Enter the year: ')))
sys.stdout = open(name + '_IMDB_Top_50_' + year + '_urllib3.txt', 'w')
url = "http://www.imdb.com/search/title?release_date=" + year + "," + year + "&title_type=feature"
r = requests.get(url).text
soup = BeautifulSoup(r, "html.parser")
article = soup.find('div', attrs={'class': 'article'}).find('h1')
print(article.contents[0] + ': ')
lister_list_contents = soup.find('div', attrs={'class': 'lister-list'})
i = 1
movieList = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})
for div in tqdm(movieList):
    print(str(i) + '.')
    header = div.findChildren('h3', attrs={'class': 'lister-item-header'})
    for items in header:
        title = header[0].findChildren('a')
        print('Movie: ' + str(title[0].contents[0]))
    genre = div.findChildren('span', attrs={'class': 'genre'})
    genre_text = genre[0].text.encode('utf-8').decode('ascii', 'ignore')
    print('Genre: ' + genre_text.strip('\n'))
    p_all = div.findAll('p', attrs={'class': 'text-muted'})
    desc = p_all[1].text.encode('utf-8').decode('ascii', 'ignore')
    print('Description: ' + desc.strip('\n'))
    i += 1
