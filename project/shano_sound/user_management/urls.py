from django.conf.urls import url
from user_management.views import register_view, login_view
urlpatterns = [
    url(r'^register/$', register_view, name='register'),
    url(r'^login/$', login_view, name='login')
]
