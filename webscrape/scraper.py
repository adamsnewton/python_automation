import requests, time, sys
import pandas as pd
from bs4 import BeautifulSoup

URL = "http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")
movieContainers = soup.find_all('div', class_ = 'lister-item mode-advanced')

# Lists to store the scraped data in
names = []
years = []
ratings = []
metascores = []
votes = []

for container in movieContainers:
    if container.find("div", class_ = "ratings-metascore") is not None:

        name = container.h3.a.text
        names.append(name)

        year = container.h3.find("span", class_ = "lister-item-year text-muted unbold").text
        years.append(year)

        rating = container.strong.text
        ratings.append(rating)

        metascore = int(container.find("span", class_ = "metascore").text)
        print(metascore)
        metascores.append(metascore)

        vote = container.find("span", attrs = {"name":"nv"})
        vote = int(vote["data-value"])
        votes.append(vote)

dataFrame = pd.DataFrame({'movie': names,
'year': years,
'imdb': ratings,
'metascore': metascores,
'votes': votes
})
print(dataFrame.info())

'''
movieContainers = soup.find_all('div', class_ = 'lister-item mode-advanced')
print(type(movieContainers))
print(len(movieContainers))

firstMovie = movieContainers[0]
firstName = firstMovie.h3.a.text
print(firstName)

firstYear = firstMovie.h3.find('span', class_ = 'lister-item-year text-muted unbold').text
print(firstYear)

imdbScore = firstMovie.strong.text
print(imdbScore)

firstScore = firstMovie.find('span', class_ = 'metascore favorable')
firstScore = int(firstScore.text)
print(firstScore)

firstVotes = firstMovie.find('span', attrs = {'name':'nv'})
firstVotes = int(firstVotes['data-value'])
print(firstVotes)
'''
