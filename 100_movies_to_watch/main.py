import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(url=URL)
website_html = response.text


soup = BeautifulSoup(website_html,"html.parser")
all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
# movie_list = movie_titles.reverse()
# print(movie_list)
movie_titles.reverse()
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")