from django.contrib import admin

# Register your models here.
from banana.models import models
from banana.models.models import Movie_Douban_Top250

class Movie_Douban_Top250Admin(admin.ModelAdmin):
    list_display = ['movie_name', 'director', 'to_star', 'add_date', 'rating_num', 'url']
    list_filter = ['director',]
    search_fields = ['movie_name', 'to_star']


admin.site.register(Movie_Douban_Top250, Movie_Douban_Top250Admin)