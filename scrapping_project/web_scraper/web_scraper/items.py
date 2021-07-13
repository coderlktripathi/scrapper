# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field  
from scrapy_djangoitem import DjangoItem
from product.models import Product

class WebScraperItem(DjangoItem):
    django_model = Product
