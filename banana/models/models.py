#encoding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Movie_Douban_Top250(models.Model):
    movie_name = models.CharField(u'电影名称', max_length=300, unique=True, db_index=True, blank=False)
    url = models.CharField(u'电影链接', max_length=300,db_index=True,blank=False)
    picture = models.ImageField(u'宣传海报', blank=True, default="")
    movie_time = models.CharField(u'总时长', max_length=100, blank=True, default="")
    add_date = models.DateTimeField(u'更新时间',auto_now_add=True)
    director = models.CharField(u'导演', max_length=100, default='未知')
    to_star = models.CharField(u'主演', max_length=100, default='')
    background = models.CharField(u'类型', max_length=300, default='未知')
    rating_num = models.IntegerField(u'评分', default=0)
    num_participants = models.CharField(u'参评人数', max_length=100, default='0')

    class Meta:
        db_table = "movie_douban_top250"
