from django.db import models

# Create your models here.
class Project(models.Model):
    thumbnail = models.ImageField(
      upload_to='thumbnail/images',
      null=False,
      blank=False
    )
    category = models.CharField(
      max_length=50,
      null=False,
      blank=False
    )
    title = models.CharField(
      max_length=100,
      null=False,
      blank=False
    )
    languages = models.CharField(
      max_length=300,
      null=False,
      blank=False
    )
    description = models.TextField(
      max_length=1000
    )
    demo = models.URLField(
      'Live Demo',
      max_length=200,
      null=True,
      blank=True
    )
    github_url = models.URLField(
      'GitHub Repo',
      max_length=200,
      null=True,
      blank=True
    )
    views = models.IntegerField(
      'Views', 
      null=True, 
      blank=True, 
      default=0
    )
    likes = models.IntegerField(
      'Likes', 
      null=True, 
      blank=True, 
      default=0
    )
    created_at = models.DateTimeField(
      blank=True,
      auto_now_add=True
    )

    def __str__(self) -> str:
      return f'Category: {self.category}, Project Title: {self.title}'