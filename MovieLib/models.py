from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=128)
    genre = models.CharField(max_length=128)
    release_date = models.DateField()
    price = models.DecimalField(max_digits=20, decimal_places=0)

    def __str__(self):
        return ' - '.join([self.title, self.genre, str(self.price), str(self.release_date)])



