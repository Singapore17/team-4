from django.conf.urls import url
from django.contrib import admin
from Index.views import *

urlpatterns = [
    url(r'^$', MainPage.as_view(), name="main-page"),
]
