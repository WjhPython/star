#!/usr/bin/env python
import urllib2
from lxml import etree
from banana.models.models import Movie_Douban_Top250

request = urllib2.Request("https://movie.douban.com/top250")
response = urllib2.urlopen(request)
content = response.read()
tree = etree.HTML(content)
movie_name = tree.xpath("//*[@id='content']/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span")
movie_name_list = []
for i in movie_name:
    movie_name_list.append(i.text)
movie_name = ''.join(movie_name_list)
print movie_name

Movie_Douban_Top250.objects.create(movie_name=movie_name,
                                   url='')

