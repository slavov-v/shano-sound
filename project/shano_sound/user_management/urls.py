from django.conf.urls import url
from user_management.views import RegisterView, LoginView, ProfileView, AddFriendView, FriendListView, log_out_view
urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', log_out_view, name='logout'),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
    url(r'^add-friend/$', AddFriendView.as_view(), name='add-friend'),
    url(r'^friends/$', FriendListView.as_view(), name='friends')
]
