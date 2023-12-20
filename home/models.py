from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    facebook = models.TextField()
    linkedin = models.TextField()
    twitter = models.TextField()
    linkedin = models.TextField()
    img = models.ImageField(blank=True)

    def __str__(self):
         return self.name

class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    mission = models.TextField()
    vision = models.TextField()
    history = models.TextField()
    

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    testimony = models.TextField()
    img = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title

class Contact(models.Model):
    title = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

class Job(models.Model):
    title = models.CharField(max_length=100)
    location = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    education = models.TextField()
    location = models.TextField()
    experience = models.TextField()
    requirements = models.TextField()

    def __str__(self):
        return self.title