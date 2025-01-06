from django.urls import path
from .import views

urlpatterns=[
    path('',views.index),
    path('<int:id>',views.bookdetails),
    # path('feb/',views.feb),
    # path('mar/',views.mar)
    # val=disc.get('jan')
    # return HttpResponse(value)
    
]