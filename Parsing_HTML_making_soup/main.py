from bs4 import BeautifulSoup



with open("/workspaces/Day45_Beautiful_soup4/Parsing_HTML_making_soup/website.html", "r", encoding="utf-8") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify()  )

all_anchor_tags = soup.find_all(name = "a" )

# for tag in all_anchor_tags:
#     # text = tag.getText()
#     link = tag.get("href")
#     print(link)

# heading = soup.find(name="h1", id="name").getText()
# print(heading)

# section_heading = soup.find(name="h3", class_ = "heading")
# print(section_heading.getText())

# company_url = soup.select_one(selector = "p a")
# print(company_url)

# select ID 
name = soup.select_one(selector = "#name")
print(name)

heading = soup.select(selector =".heading")
print(heading)

