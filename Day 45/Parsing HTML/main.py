from bs4 import BeautifulSoup

with open(file="website.html") as website:
    contents = website.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup)
print(soup.prettify())
print(soup.title)
print(soup.title.string)
print(soup.p) # first p in website 

