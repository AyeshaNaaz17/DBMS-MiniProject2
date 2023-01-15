from django.contrib import admin

from .models import Faculty, Conference, Journal, Event, Post, RequestPublications, Rating 


admin.site.register(Faculty)
admin.site.register(Conference)
admin.site.register(Journal)
admin.site.register(Event)
admin.site.register(Post)
admin.site.register(RequestPublications)
admin.site.register(Rating)