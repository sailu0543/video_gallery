from django.db import models

# Create your models here.
class Videoplayer(models.Model):
    title=models.CharField(max_length=1000)
    video=models.FileField(upload_to='videos/')
    thumbnail=models.ImageField(upload_to='thumbnail')



    def __str__(self):
        return self.title
