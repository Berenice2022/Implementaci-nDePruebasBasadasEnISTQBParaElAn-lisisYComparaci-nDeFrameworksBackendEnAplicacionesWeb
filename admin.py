from django.contrib import admin
from .models import Post, Like, Comment, Event, Interest, User
# Register your models here.

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(User)
admin.site.register(Interest)
admin.site.register(Comment)
admin.site.register(Event)
