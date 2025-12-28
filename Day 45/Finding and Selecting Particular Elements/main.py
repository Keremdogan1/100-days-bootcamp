from bs4 import BeautifulSoup

with open(file="website.html") as website:
    contents = website.read()

soup = BeautifulSoup(contents, "html.parser")

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(f"\n{heading.string}")

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))

company_name = soup.select_one(selector="p a")
print(company_name)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(selector=".heading")
print(headings)