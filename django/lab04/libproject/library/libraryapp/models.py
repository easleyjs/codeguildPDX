from django.db import models

# Create your models here.
# Book: a model representing a book, with a title, publish date, and an author (many-to-many foreign key)
# Author: a model representing an author of a book, one author can have multiple books
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    authored_by = models.ManyToManyField(Author)
    status = models.CharField(max_length=50, null=True)
    checked_out_by = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title
