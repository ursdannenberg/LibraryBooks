#from django.shortcuts import render
from django.views import generic
from .models import Book

# Create your views here.
class IndexView(generic.ListView):
    template_name = "library/index.html"
    context_object_name = "book_list"

    def get_queryset(self):
        """
        Return all list of all books.
        """
        return Book.objects.all()
