from django.urls import path
from .import views

urlpatterns=[
    path('',views.review),
    # path('<int:id>',views.bookdetails),
    ]