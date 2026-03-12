from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.title


class List(models.Model):
    id = models.AutoField(primary_key=True)
    list = models.CharField(max_length=50)

    def __str__(self):
        return self.list
    
#class Demo(models.Model):
    #title = models.CharField(max_length=100)



