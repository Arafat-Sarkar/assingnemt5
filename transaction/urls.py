from django.urls import path
from . import views

urlpatterns = [
    path('deposite/', views.DepositeMoney.as_view(), name='deposit'),
]