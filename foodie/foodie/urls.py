from django.conf.urls import url, include
from django.contrib import admin
from Index import views

urlpatterns = [
	url(r'^', include('Index.urls')),
    url(r'^reporter/', include('Reporter.urls')),
    url(r'^admin/', admin.site.urls),
]
