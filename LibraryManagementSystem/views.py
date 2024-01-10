
from django.shortcuts import render
from book.models import Book
from category.models import Category
def home(request, category_slug = None):
    book = Book.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        book = Book.objects.filter(categories  = category)
    categories = Category.objects.all()
    return render(request, 'home.html', {'book' : book, 'category' : categories})