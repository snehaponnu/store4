from django.db import models
from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

from django.db import models
# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    field_name = models.URLField()


    def get_url(self):
        return reverse('collegeapp1:courses_by_department',args=[self.slug])
    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural='departments'
    def __str__(self):
           return '{}'.format(self.name)

class Course(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    department= models.ForeignKey(Department,on_delete=models.CASCADE)
    available = models.BooleanField(default=True)


    # def get_url(self):
    #     return reverse('shop:prodCatdetail',args=[self.category.slug,self.slug])
    class Meta:
        ordering=('name',)
        verbose_name='course'
        verbose_name_plural='courses'
    def __str__(self):
        return '{}'.format(self.name)

from django.db import models

# Create your models here.



GENDER_CHOICES = (
    ('male', 'male'),
    ('female', 'female'),
)


class Form(models.Model):
    name=models.CharField(max_length=250)
    dob=models.DateField()
    gender=models.CharField(max_length=6, choices=GENDER_CHOICES)
    email=models.EmailField()
    phone=models.IntegerField()
    address= models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    department =models.CharField(max_length=250)
    purpose =models.CharField(max_length=250)
    material =models.BooleanField(null=True)
    age =models.IntegerField()
    def __str__(self):
        return self.name