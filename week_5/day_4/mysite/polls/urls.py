from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.hello,name='index'), # include the urls.py from the polls application
]