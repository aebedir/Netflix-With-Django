from django.db import models

# Create your models here.

class Kategori(models.Model):
    isim = models.CharField(max_length=100)

    def __str__(self):
        return self.isim
    
class Movie(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True)
    isim = models.CharField(max_length=100)
    resim = models.ImageField(upload_to='filmler/')

    def __str__(self):
        return self.isim