from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.contactview,name='contactview'),
    path('delete/<int:contactid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update')
]