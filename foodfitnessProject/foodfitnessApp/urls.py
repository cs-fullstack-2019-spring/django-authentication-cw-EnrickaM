from django .urls import path
from .import views
# this code below allows you to direct to different pages.

urlpatterns=[
    path("", views.index, name='index'),
    path('newuser/',views.newuser,name='newuser'),
    path("createnewuser/",views.createnewuser,name='createnewuser'),
]