from django.db import models
# Create your models here.

GENDER_CHOICES = [
    ('M',"Male"),
    ('F',"Female"),
    ('0',"Other")
]

class School(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name



class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    course = models.CharField()
    dob = models.DateField()
    address = models.CharField(max_length=40)
    is_present = models.BooleanField()
    gender = models.CharField(choices=GENDER_CHOICES,null=True,blank=True)
    institution = models.ForeignKey(School,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name + " " + self.phone
    
    @property
    def age(self):
        from datetime import date
        born = self.dob
        today = date.today()
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

        return age

        
