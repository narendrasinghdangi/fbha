from django.db import models

# Create your models here.

class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    email=models.CharField(max_length=50,default="")
    passw=models.CharField(max_length=50,default="")

    def __str__(self):
        return self.email
