from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    published_year = models.IntegerField()
    isbn = models.CharField(max_length=13)
    publisher = models.CharField(max_length=255)
    pages = models.IntegerField()
    language = models.CharField(max_length=50)
    description = models.TextField()
    cover_image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)
