from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=20,null=True)
    email=models.EmailField(null=True)
    phoneno=models.IntegerField(null=True)
    image=models.ImageField(null=True)
    def __str__(self):
        return self.name
    
class savefile(models.Model):
    file=models.FileField()

