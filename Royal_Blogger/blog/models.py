from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    video = models.FileField(upload_to='images/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=255, default='uncategorized')
    created_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, blank=True, related_name='blog_posts')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-created_on']

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"pk": self.pk})

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='images/', null=True, blank=True)
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

# class BlogCategories(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name
    
#     def get_absolute_url(self):
#         return reverse("blog:home")

#     class Meta:
#         verbose_name_plural = "Blog Categories"
#         ordering = ['name']
