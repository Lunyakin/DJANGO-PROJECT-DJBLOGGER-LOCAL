from djblogger.blog.views import *
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name='homepage')
]