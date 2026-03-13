from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class List(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="lists",
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=100,
        default="Sin nombre"
    )

    def __str__(self):
        return self.name


class Task(models.Model):
    list = models.ForeignKey(
        List,
        on_delete=models.CASCADE,
        related_name="tasks",
        null=True,
        blank=True
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title