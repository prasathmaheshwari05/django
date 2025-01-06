from django.urls import path
from .import views

urlpatterns=[
    path('',views.ProfileCreateView.as_view()),
    # path('<int:id>',views.bookdetails),
    path('list',views.ProfileViewList.as_view())
    ]