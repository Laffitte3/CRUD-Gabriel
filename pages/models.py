from django.db import models

# Create your models here.


class Post(models.Model):

    title=models.CharField(max_length=40)
    description=models.TextField()
    image=models.ImageField(upload_to="media",blank=True)
    author= models.ForeignKey("auth.User", on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):

        return self.title
    

class Home(models.Model):

    titulo=models.CharField(max_length=40)
    image=models.ImageField(upload_to="photos/background")


    def __str__(self):

        return self.titulo
