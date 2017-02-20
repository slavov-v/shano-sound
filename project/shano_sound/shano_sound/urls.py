"""shano_sound URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from user_connections import views as user_connections_views


urlpatterns = [
    url(r'', include('user_management.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'', include('user_connections.urls')),
    url(r'', include('user_management.urls')),
    url(r'thanks', user_connections_views.thanks),
]
