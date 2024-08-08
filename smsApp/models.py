from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Donor(models.Model):
    GENDER = (
        ('Female', 'Female'),
        ('Male', 'Male'),
    )
    firstname = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    phone = models.CharField(max_length=20, null=False)
    gender = models.CharField(max_length=6,choices=GENDER, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.firstname}'
    
class School (models.Model):
    LOCATION = (
        ('Nairobi', 'Nairobi'),
        ('Kisumu', 'Kisumu'),
        ('Nakuru', 'Nakuru'),
        ('Naivasha', 'Naivasha'),
        ('Mombasa', 'Mombasa'),
    )
    schoolname = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    location = models.CharField(max_length=30,choices=LOCATION, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.schoolname}'

class Student(models.Model):
    GENDER = (
        ('Female', 'Female'),
        ('Male', 'Male'),
    )
    LEVELOFSTUDY = (
        ('Primary','Primary'),
        ('Secondary','Secondary'),
        ('Tertiary','Tertiary'),
    )
    POSITION = (
        ('SingleOrphan', 'SingleOrphan'),
        ('DoubleOrphan', 'DoubleOrphan'),
        ('Disabled', 'Disabled'),
    )
    STATUS = (
        ('New','New'),
        ('Contunuing','Contunuing'),
        ('Discontinued','Discontinued'),
        ('Completed','Completed'),
    )

    firstname = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=25, null=False)
    gender = models.CharField(max_length=100, choices=GENDER, null=False)
    levelofstudy = models.CharField(max_length=30,choices=LEVELOFSTUDY,null=False)
    position = models.CharField(max_length=30,choices=POSITION, null=False)
    status = models.CharField(max_length=30,choices=STATUS,null=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    DateofBirth = models.DateField(null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.firstname}'
    
class Employee(models.Model):
    GENDER = (
        ('Female', 'Female'),
        ('Male', 'Male'),
    )
    DEPT =(
        ('Finance', 'Finance'),
        ('Records', 'Records'),
        ('Research', 'Research'),
        ('HR', 'HR'),
    )
    firstname = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=25, null=False)
    gender = models.CharField(max_length=100, choices=GENDER, null=False)
    department = models.CharField(max_length=100, choices=DEPT, null=False)
    DateofBirth = models.DateField(null=False)
    Date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.firstname}'
    
