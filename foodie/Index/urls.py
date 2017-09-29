from django.conf.urls import url
from django.contrib import admin
from Index.views import *

urlpatterns = [
    url(r'^$', DonationFormSubmission.as_view(), name="main-page"),
]
