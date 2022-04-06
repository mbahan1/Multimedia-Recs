from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENRE_CHOICES = (	
    ("act", "Action"),
	("com", "Comedy"),	
    ("comdram", "Comedy/Drama"),
	("crim", "Crime/Mystery"),
	("doc", "Documentary"),    
    ("docdram", "Docudrama"),
	("dram", "Drama"),
	("histdram", "Historical Drama"),
	("music", "Musical"),
	("news", "News"),
	("police", "Police Procedural"), 
	("reality", "Reality"),
	("romcom", "Romantic Comedy"),
	("romdram", "Romantic Drama"),    
	("scifi", "Science Fiction"),
	("sitcom", "Sitcom"),
	("susp", "Suspense"),
)
STREAM_CHOICES = (
    ("acron", "Acorn TV"),
    ("amaz", "Amazon Prime TV"),
    ("amc", "AMC+"),
    ("appl", "Apple TV+"),
    ("att", "AT&T"),
    ("brit", "BritBox"),
    ("cbs", "CBS"),
    ("dirtv", "DirecTV"),
    ("dis", "Disney+"),
    ("fubo", "Fubo"),
    ("hbo", "HBO Max"),
    ("hoop", "Hoopla"),
    ("hulu", "Hulu+"),
    ("kan", "Kanopy"),
    ("nbc", "NBC"),
    ("net", "Netflix"),
    ("para", "Paramount+"),
    ("show", "Showtime"),
    ("star", "Starz"),
    ("tou", "YouTube"),
    ("tcm", "TCM"),
)

class Review(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE) #1:m
    date_written = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.body

class Show(models.Model):
    title = models.CharField(max_length=150)
    first_aired = models.IntegerField()
    last_aired = models.IntegerField()
    genre = models.CharField(max_length=50, choices = GENRE_CHOICES)
    stream_service = models.CharField(max_length=250, choices = STREAM_CHOICES)
    img = models.CharField(max_length=500)
    description = models.TextField()
    thumbs = models.IntegerField()
    user = models.ManyToManyField(User) #m:m
    reviews = models.ForeignKey(Review, null=True, blank=True, on_delete=models.CASCADE) #1:m
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['thumbs']