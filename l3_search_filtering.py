import re
from bs4 import BeautifulSoup


with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# Get the tag attributes
tag = doc.find("option") # Find the first option tag
print("Tag attributes \n", tag.attrs, "\n")

# Find multiple tags
tags = doc.find_all(["p", "div", "li"])
print("multiple tag names \n", tags, "\n")

# Search a text
text = doc.find_all("option", text="Undergraduate")
print("Search a text \n", text, "\n")

# Search a value
value = doc.find_all("option", value="undergraduate")
print("Search a value \n", value, "\n")

# Search a class, please notice, class is a reserved word in Python so we use class_
tags_class = doc.find_all(class_="btn-item")
print("Search a class \n", tags_class, "\n")

# Search a class with regular expression
tags_regex = doc.find_all(text=re.compile("\$.*")) # This simplifies the steps to find the price of a GPU shown in l2_parse_website.py
for tag_regex in tags_regex:
    print("Search a text with regular expression \n", tag_regex.strip(), "\n")

# Limit search results
tags_regex = doc.find_all(text=re.compile("\$.*"), limit=1)
for tag_regex in tags_regex:
    print("Limit search \n", tag_regex.strip(), "\n")

