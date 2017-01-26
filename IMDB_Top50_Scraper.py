import urllib2
import sys
from BeautifulSoup import BeautifulSoup
from tqdm import tqdm
import datetime
current_year = int(datetime.datetime.now().year)
for year in tqdm(range(1898, current_year)):
    sys.stdout = open('DataSets//IMDB_Top_50_' + str(year) + '.txt', 'w')
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    url = "http://www.imdb.com/search/title?release_date=" + str(year) + "," + str(year) + "&title_type=feature"
    ourUrl = opener.open(url).read()
    soup = BeautifulSoup(ourUrl)
    article = soup.find('div', attrs={'class': 'article'}).find('h1')
    print article.contents[0] + ': '
    lister_list_contents = soup.find('div', attrs={'class': 'lister-list'})
    i = 1
    movieList = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})
    for div in tqdm(movieList):
        print str(i) + '.',
        header = div.findChildren('h3', attrs={'class': 'lister-item-header'})
        for items in header:
            print 'Movie: ' + str((header[0].findChildren('a'))[0].contents[0])
        if div.findChildren('span', attrs={'class': 'genre'}):
            genre = div.findChildren('span', attrs={'class': 'genre'})
            print 'Genre: ' + genre[0].text.encode('utf-8').decode('ascii', 'ignore')
        if div.findChildren('p', attrs={'class': 'text-muted'}):
            description = div.findChildren('p', attrs={'class': 'text-muted'})
            print 'Description: ' + description[0].text.encode('utf-8').decode('ascii', 'ignore')
        i += 1
