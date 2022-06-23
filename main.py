# The goal of this code is to parse data about top 250 imdb films including - place, title, year and cast.
# Second goal of this code is to not just get those data in terminal but also export it in CSV format.

import requests
from bs4 import BeautifulSoup as BS
import re
import pandas as pd


# Get imdb top 250 movies data.
url = "https://www.imdb.com/chart/top"
response = requests.get(url)
soup = BS(response.text, 'html.parser')
movies = soup.select("td.titleColumn")
crew = [i.attrs.get('title') for i in soup.select("td.titleColumn a")]

# Create an empty list for storing information about movie.
list = []

# Looping through movies to extract information about them.
for index in range(0, len(movies)):

# Separating movie into title, year.
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.',''))
    movie_title = movie[len(str(index))+1:-6]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"place": place,
            "movie_title": movie_title,
            "year": year,
            "star_cast": crew[index],
            }
    list.append(data)

# Printing movie details with its rating.
for movie in list:
    print(movie['place'], '-', movie['movie_title'], '('+movie['year'] + ')-', 'Starring', movie['star_cast'])

# Use pandas to extract all data in CSV file that will create CSV file in the project folder.
df = pd.DataFrame(list)
df.to_csv('imdb_top_250_movies.csv', index = False)
