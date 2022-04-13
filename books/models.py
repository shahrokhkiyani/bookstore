from django.db import models

class Book(models.Model):
    
    # name, description, author, creator, date_time published, cover, publisher, year created
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()
    #? desimal_places number of persian -> "ashar's" in nubmer

    #? max_digits number of digits in number like -> 1234.56

    #? For money we use DeciamlFields
    price= models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.title