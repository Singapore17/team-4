from django.conf.urls import url
from django.contrib import admin
from Reporter.views import *

urlpatterns = [
    url(r'^mail-all$', SendEmailToBenefactors.as_view(), name="send-mail-benefactors"),
]
