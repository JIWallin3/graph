from django.db import models


# Create an Author model
class Author(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

    def __str__(self):
        return self.last_name + ", " + self.first_name


# Create a Book model
class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()

    def __str__(self):
        return self.title
