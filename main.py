import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

soup = BeautifulSoup(requests.get(URL).text, "html.parser")
article = [_.getText() for _ in soup.find_all(name="h3", class_="title")]

print(f"The top 100 movies to watch from the best to the list:")
with open("movies to watch.txt", "w") as file:
    for n in range(0, len(article)):
        movies_watch = (article[-n - 1])
        print(movies_watch)
        file.write(movies_watch + "\n")
