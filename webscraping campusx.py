import pandas as pd
import requests
from bs4 import BeautifulSoup

p = requests.get('https://www.ambitionbox.com/list-of-companies?page=1').text
#print(p)

# ab ham ye sab data beautifulsoup ko dedenge
soup = BeautifulSoup(p,'html.parser')   # ye parser he lxml iske wajah se ham traverse karpaenge easily

#print(soup.prettify())

s3= soup.find_all('h2')[0].text
#print(s3)

##s = []
#for i in soup.find_all('h2'):
    #print(i.text.strip())  # ye strip lagae takee gaaps sab haat jae aur poper sahi format me ae
    ##s.append(i.text.strip())

#print(s)

#for i in soup.find_all('p'):
    #print(i.text.strip()) # isse dikat he ki sirf vo rating jo hame chahiye vo nahi aega uske saath saath sab ajaega

for i in soup.find_all('p',class_='rating'):
    print(i.text.strip())

print()

for i in soup.find_all('a',class_='review-count'):
    print(i.text.strip())

print()

company = soup.find_all('div',class_="company-content-wrapper")
# lekin isse acha he ki har div ke andar ghuske usme se find('p/a/h2') karke fir lekeao fir isse sab ekhi loop me hojaega
print(company[0].find_all('p',class_='infoEntity')[1].text.strip())


print()





names = []
ratings = []
reviews = []
for i in soup.find_all('div',class_="company-content-wrapper"):
    names.append(i.find('h2').text.strip())
    #print(names)
    ratings.append(i.find('p',class_='rating').text.strip())
    #print(ratings)
    reviews.append(i.find('a',class_='review-count').text.strip())

    #print(reviews)

# iske baad sabko dictionary ke form me convert karo aur fir usko use karke dataframe bana lo

