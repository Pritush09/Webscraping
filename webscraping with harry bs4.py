import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"


# Step 1 :  Get the html
r = requests.get(url)

# if u want the html content
htmlcontent = r.content

# print(htmlcontent)

# Step 2 :  Parse the html
soup = BeautifulSoup(htmlcontent,"html.parser")
#print(soup.prettify)


# Step 3 :  Html Tree travarsal
# html is itself a form of tree
###
#Commonly used obejects
# 1. Tag
# 2. NavigableString
# 3. BeautifulSoup
# 4. comment
#print(type(soup))
#print(type(title))
#print(type(title.string))

# geting the title of the html page
title = soup.title

# geting the paragraph from the page
paras = soup.findAll("p")
# print(paras)

# getting all the anchor tags
anchor = soup.findAll("a")
# print(anchor)

# Getting the first element from the html page
print(soup.find("p"))

# getting the classes of any element in the html page
print(soup.find("p")["class"])

# getting the elements with class lead
print(soup.find("p",class_="lead"))

