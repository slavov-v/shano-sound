from django.conf.urls import url
from user_management.views import register_view, login_view, ProfileView, AddFriendView, FriendListView, log_out_view
urlpatterns = [
    url(r'^register/$', register_view, name='register'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', log_out_view, name='logout'),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
    url(r'^add-friend/$', AddFriendView.as_view(), name='add-friend'),
    url(r'^friends/$', FriendListView.as_view(), name='friends')
]
