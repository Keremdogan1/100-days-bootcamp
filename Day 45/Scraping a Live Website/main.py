from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

unsorted_article_links = soup.select(selector=".title .titleline span a")
unsorted_article_upvotes = soup.select(selector=".subline .score")

article_texts = [elem.get_text() for elem in unsorted_article_links]
article_links = [tag.get("href") for tag in unsorted_article_links]

max = 0
max_index = 0

article_upvotes = [int(elem.get_text().split()[0]) for elem in unsorted_article_upvotes]
for i in range(len(article_upvotes)):
    if article_upvotes[i] > max:
        max = article_upvotes[i]
        max_index = i

print(f"{article_texts}\n")
print(f"{article_links}\n")
print(article_upvotes)

print(f"{max_index + 1}. article(Name: {article_texts[max_index]}, Link:{article_links[max_index]}) is most upvoted  with {max} upvotes!")