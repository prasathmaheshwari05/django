from django.urls import path
from .import views

urlpatterns=[
    path('jan/',views.home,jan='today is hoilday'),
    # path('feb/',views.feb),
    # path('mar/',views.mar)
    # val=disc.get('jan')
    # return HttpResponse(value)
    
]