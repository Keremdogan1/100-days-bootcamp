from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()

soup = BeautifulSoup(response.content.decode("utf-8"), "html.parser")

movies = soup.select(selector="h3", class_="title")
movies_texts = [f"{elem.get_text()}\n" for elem in movies]
movies_texts.reverse()

print(movies_texts)
with open("movies.txt", "w", encoding="utf-8") as file:
    file.writelines(movies_texts)