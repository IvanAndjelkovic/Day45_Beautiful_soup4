from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')


articles = soup.find_all(class_="titleline")
article_texts = []
article_links = []
article_upvotes = []
for article in articles:
    article_tag = article.find("a")
    article_text = article_tag.getText()
    article_link = article_tag.get("href")
    article_upvote = article.find_next(class_="score").getText() 
    article_texts.append(article_text)
    article_links.append(article_link)
    article_upvotes.append(int(article_upvote.split()[0]))

print(article_texts)
print(article_links)
print(article_upvotes)
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])
print(article_upvotes[largest_index])





# with open("/workspaces/Day45_Beautiful_soup4/Parsing_HTML_making_soup/website.html", "r", encoding="utf-8") as f:
#     content = f.read()

# soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify()  )

# all_anchor_tags = soup.find_all(name = "a" )

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
# name = soup.select_one(selector = "#name")
# print(name)

# heading = soup.select(selector =".heading")
# print(heading)

