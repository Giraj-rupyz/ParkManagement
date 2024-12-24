from django.urls import path
from . import views


urlpatterns=[
    path("visitors/", views.ListVisitor.as_view()),
    path("book/", views.CreateTicket.as_view()),
    path('discount/', views.SetDiscount.as_view()),
    path('offers/', views.ViewOffers.as_view())
]