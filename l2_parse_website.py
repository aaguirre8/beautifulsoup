"""
Please notice, Some websites don't allow web scraping due to antibot policies
"""

from bs4 import BeautifulSoup
import requests


# url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"
url = "https://www.newegg.ca/gigabyte-geforce-rtx-4090-gv-n4090gaming-oc-24gd/p/N82E16814932550"

# Send a request to the url
result = requests.get(url)
# print("result of the request: \n", result.text)

# html parser
doc = BeautifulSoup(result.text, "html.parser")
# print("doc: \n", doc.prettify())

# find the price of the GPU
prices = doc.find_all(text="$") # find all the tags with $ sign
print("prices: \n", prices)
parent = prices[0].parent # find the parent of the first $ sign, get the tree structure of the html document
print("parent: \n", parent)

# So, the tag named strong is the parent of the price
strong = parent.find("strong")
print("strong: \n", strong.string)