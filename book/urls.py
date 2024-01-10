from django.urls import path
from . import views

urlpatterns = [
    path('details/<int:id>/', views.DetailBookView.as_view(), name='detail_book'),
    path('profile/', views.profileView, name='profile'),
    path('borrow/<int:id>/', views.borrow, name='borrow'),
    path('returned/<int:id>/', views.returned, name='returned'),
]