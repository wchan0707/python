# coding: UTF-8
import urllib2
import sys, codecs

from bs4 import BeautifulSoup

sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

url = "http://wolf-fun.secret.jp/?%E6%9C%80%E8%BF%91%E3%81%AE%E3%82%A6%E3%83%AB%E3%83%95%E6%B3%A8%E7%9B%AE%E6%A0%AA"

html = urllib2.urlopen(url)

# html‚ðBeautifulSoup‚Åˆµ‚¤
soup = BeautifulSoup(html, "html.parser")

soup2= soup.find(class_="ie5")

soup3= soup.find_all(class_="style_td")

for tag in soup3:
	print(tag.string)
