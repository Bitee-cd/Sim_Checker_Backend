from django.urls import path
from . import views

urlpatterns=[
    path('',views.ListSimApp.as_view()),
     path('<int:pk>/', views.DetailSimApp.as_view()),
]

