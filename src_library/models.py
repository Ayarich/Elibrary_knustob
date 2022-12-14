from django.db import models

from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User




# Create your models here.
class Category(models.Model):
    name = models.CharField('Categories', max_length=50)
    slug = models.SlugField(max_length = 50)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField(max_length=100)
    cover_image = models.ImageField(upload_to = 'img', blank = True, null = True)
    author = models.CharField(max_length=50)
    summary = models.TextField()
    category = models.ManyToManyField(Category, related_name='books')
    pdf = models.FileField(upload_to='pdf')
    engineering_books = models.BooleanField(default=False)
    Ksb_books = models.BooleanField(default=False)
    hesa_books = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class BookSearch(models.Model):
    name_of_book = models.CharField(max_length=100)
    def __str__(self):
        return self.name_of_book

class Video(models.Model):
    title = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()
    
    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-added']


class Student(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="profile1.png", null=True, blank=True,upload_to="profilepics")
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	

	def __str__(self):
		return self.name

