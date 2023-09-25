from bs4 import BeautifulSoup


# Read the HTML file
with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# Print to see how does it look like a python obj
print("python obj: \n", doc.prettify(), "\n")  # prettify gives identation html file

# Find things by the tag name
tag = doc.title
print("tag: \n", tag, "\n")

# Access the tag content as a string
print("tag.string: \n", tag.string, "\n")

# Modify the tag content inplace
tag.string = "hello"
print("modified html file content : \n", doc.prettify(), "\n")

# Find all the tags with the same name
tags = doc.find_all("a")  # a is the tag name for links in a htnl file
print("tags: \n", tags, "\n")

# How to access nested tags
nested_tags = doc.find_all("p")[0]
print("nested_tags: \n", nested_tags, "\n")
