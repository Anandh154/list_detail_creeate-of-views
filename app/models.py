from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    SCname=models.CharField(max_length=100)
    SCprincipal=models.CharField(max_length=50)
    SClocation=models.CharField(max_length=100)
    def __str__(self):
        return self.SCname
    
    def get_absolute_url(self):
        return reverse("SchoolDetailView",kwargs={'pk':self.pk})
class Student(models.Model):
    sname=models.CharField(max_length=100)
    sage=models.IntegerField()
    SCname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='NTR')

    def __str__(self):
        return self.sname
    


