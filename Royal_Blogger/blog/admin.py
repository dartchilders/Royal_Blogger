from django.contrib import admin
from .models import Post, UserProfile
# from .models import BlogCatgories

admin.site.register(Post)
admin.site.register(UserProfile)
# admin.site.register(BlogCategories)

