from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=20)
    bio = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.TextField

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.TextField(max_length=100 , default='project')
    description = models.CharField(max_length=250)
    technology = models.TextField(max_length=50)
    status = models.CharField(max_length=20 ,default='done')
    source = models.TextField(default='link')
    

    def __str__(self):
        return self.name
