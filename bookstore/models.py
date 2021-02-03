from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Books(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=150)
    book_link = models.URLField()
    description = models.TextField()
    id_book = models.IntegerField()
    date_download = models.DateTimeField(auto_now_add=True)
    image_link = models.URLField()
    isbn = models.CharField(max_length=50)

    def __str__(self):
        return self.title
