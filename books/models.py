from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Book(models.Model):

    # name, description, author, creator, date_time published, cover, publisher, year created

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()
    # ? desimal_places number of persian -> "ashar's" in nubmer

    # ? max_digits number of digits in number like -> 1234.56

    # ? For money we use DeciamlFields
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cover = models.ImageField(upload_to="covers/", blank=True)

    def __str__(self):
        return f"{self.title}, {self.author}, {self.price}"

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.id])


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()

    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.text}'
    