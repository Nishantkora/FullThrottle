__author__ = 'Nishanth'
from django.conf.urls import url
from users import views as user


urlpatterns = [
    url(r'^users$', user.UserView.as_view())
]
