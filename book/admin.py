from django.contrib import admin

from .models import Book, BorrowedBook,Review,Profile
admin.site.register(Book)
admin.site.register(BorrowedBook)
admin.site.register(Review)
admin.site.register(Profile)