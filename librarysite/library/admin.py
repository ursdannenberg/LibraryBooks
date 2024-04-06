from django.contrib import admin

from .models import Book, Library

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "return_date", "return_next_week", "extendable"]
    
admin.site.register(Book, BookAdmin)
admin.site.register(Library)