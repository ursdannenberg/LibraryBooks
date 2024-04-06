import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    return_date = models.DateField("Return date")
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    extendable = models.BooleanField("Can the loan be extended?", default=True)
    
    def __str__(self):
        return self.title
    
    @admin.display(
        boolean=True,
        ordering="return_date",
        description="Return next week?",
    )
    def return_next_week(self):
        return self.return_date <= timezone.now().date() + datetime.timedelta(days=7)