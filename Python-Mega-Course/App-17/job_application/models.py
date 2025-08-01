from django.db import models

class Form(models.Model):
    firstname=models.CharField(max_length=80)
    lastname=models.CharField(max_length=80)
    email=models.CharField()
    date=models.DateField()
    occupation = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

