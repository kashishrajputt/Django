from django.db import models
from django.utils import timezone

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
