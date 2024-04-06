import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    return_date = models.DateTimeField("Return date")
    library = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
    def return_next_week(self):
        return self.return_date <= timezone.now() + datetime.timedelta(days=7)