
!pip install selenium
!pip install splinter

from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time

#Choose the executable path 
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

# Visit web page
url = "https://mars.nasa.gov/news/"
browser.visit(url)

html = browser.html
soup = bs(html,"html.parser")

news_title = soup.find("div",class_="content_title").text
news_paragraph = soup.find("div", class_="article_teaser_body").text
print(f"Title: {news_title}")
print(f"Para: {news_paragraph}")

### MARS IMAGES

url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url_image)

from urllib.parse import urlsplit
base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url_image))
print(base_url)

# grab image
xpath = "//*[@id=\"page\"]/section[3]/div/ul/li[1]/a/div/div[2]/img"

#Use splinter to click on the mars featured image
#to bring the full resolution image
results = browser.find_by_xpath(xpath)
img = results[0]
img.click()


#get image url using BeautifulSoup
image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(image_url)
html = browser.html
soup = bs(html, "html.parser")

image = soup.find("img", class_="thumb")["src"]
featured_image_url = "https://www.jpl.nasa.gov" + image
print(featured_image_url)

##Weather
url_weather = "https://twitter.com/marswxreport?lang=en"
browser.visit(url_weather)

html_weather = browser.html
soup = bs(html_weather, "html.parser")
temp = soup.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"})
mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
print(mars_weather)
temp

##Facts
url_Marsfacts = "https://space-facts.com/mars/"
table = pd.read_html(url_Marsfacts)
table[0]

#Hemispheres

url_hemisphere = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url_hemisphere)

#Getting the base url
hemisphere_base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url_hemisphere))
print(hemisphere_base_url)

import time 
hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemispheres_url)
html = browser.html
soup = bs(html, "html.parser")
mars_hemisphere = []

products = soup.find("div", class_ = "result-list" )
hemispheres = products.find_all("div", class_="item")

for hemisphere in hemispheres:
    title = hemisphere.find("h3").text
    title = title.replace("Enhanced", "")
    end_link = hemisphere.find("a")["href"]
    image_link = "https://astrogeology.usgs.gov/" + end_link    
    browser.visit(image_link)
    html = browser.html
    soup=bs(html, "html.parser")
    downloads = soup.find("div", class_="downloads")
    image_url = downloads.find("a")["href"]
    mars_hemisphere.append({"title": title, "img_url": image_url})

return mars_hemisphere
