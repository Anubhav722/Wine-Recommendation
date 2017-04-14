# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Wine, Review
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('wine', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ('pub_date', 'user_name')
    search_fields = ('comment', 'user_name', )

admin.site.register(Wine)
admin.site.register(Review, ReviewAdmin)
