from django.db import models
from django.contrib.auth.models import User
from category.models import Category
from accounts.models import UserAccount
from transaction.models import Transaction

class Book (models.Model):
    categories = models.ManyToManyField(Category)   
    image = models.ImageField(upload_to='book/media/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    borrow_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) :
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review')
    name = models.CharField(max_length=30)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reviews by {self.name}"
    
class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    account = models.ForeignKey(UserAccount,  on_delete = models.CASCADE)
    borrowing_date = models.DateTimeField(auto_now_add=True)
    balance_after_borrow = models.DecimalField(decimal_places=2, max_digits = 12, null= True, blank= True)
    returned = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, null= True, blank= True)

    def __str__(self):
        return f"Reviews by {self.account.id} __ {self.book.title}"

class Profile(models.Model):
    account = models.OneToOneField(UserAccount, on_delete=models.CASCADE, null= True, blank= True)
    borrowed_book = models.ManyToManyField(BorrowedBook)

    def __str__(self):
        return f"Profile: {self.account}"