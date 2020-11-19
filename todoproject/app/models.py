from django.db import models
from datetime import date
class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(verbose_name="Tarea", max_length=150)
    task_description = models.CharField(verbose_name="descripcion", max_length=250)
    date = models.DateTimeField()

    def __str__(self):
        return self.task_name + " - "  + str(self.date)

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text=models.TextField()
    pub_date=models.DateField()
    mod_date=models.DateField()
    authors=models.ManyToManyField(Author)
    number_of_comments=models.IntegerField()
    number_of_pingbacks=models.IntegerField()
    rating=models.IntegerField()

    def __str__(self):
        return self.headline
