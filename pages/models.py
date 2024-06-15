from django.db import models

# Create your models here.


class Post(models.Model):

    title=models.CharField(max_length=40)
    description=models.TextField()
    #image=models.ImageField(default='null' ,upload_to="photos/%y/%m/%d/")
    author= models.ForeignKey("auth.User", on_delete=models.CASCADE, null=False, default=None)


    def __str__(self):

        return self.title
