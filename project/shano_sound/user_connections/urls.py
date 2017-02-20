from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'connection_panel', views.ConnectionView.as_view(),
        name='connection_view'),
]
