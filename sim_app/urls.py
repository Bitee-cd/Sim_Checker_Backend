from django.urls import path
from . import views

urlpatterns=[
    path('',views.ListSim.as_view()),
    path('sim/',views.ListPhoneNumber.as_view()),
     path('<int:pk>/', views.DetailSimApp.as_view()),
     path('find/<str:number_>/', views.FindSim.as_view()),
]

