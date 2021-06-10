from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    enrollment_num = models.IntegerField()

    def __str__(self):
        return self.first_name
