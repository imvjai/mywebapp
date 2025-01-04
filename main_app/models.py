from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_url = models.URLField()
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
