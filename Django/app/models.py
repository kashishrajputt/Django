from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class AppVarity(models.Model):
    Type_Choice = [
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KL','KIWI'),
        ('PL','PLAIN'),
        ('EL','ELAICHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'apps/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices = Type_Choice)
    description = models.TextField(default='')
    

def __str__(self):
    return self.name

#one to many model: a single chai can have multiple reviews
class Review(models.Model):
    app_varity = models.ForeignKey(AppVarity, on_delete=models.CASCADE, related_name = 'reviews')
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    

# mamy to many 
class Store(models.Model):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(AppVarity, related_name = 'store')

    def __str__(self):
        return self.name

#one to one
class Certificate(models.Model):
    chai = models.OneToOneField(AppVarity, on_delete=models.CASCADE, related_name ='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.name.chai}'
