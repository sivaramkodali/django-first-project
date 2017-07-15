from django.conf.urls import url
from first_app import views


app_name = 'first_app'

urlpatterns = [
    url(r'^first_page/',views.first_page,name='first_page'),
    url(r'^second_page/',views.second_page,name='second_page'),
    url(r'^users_page/',views.users_page,name='users_page'),
    url(r'^forms_page/',views.forms_page,name='forms_page'),
    url(r'^create_users/',views.create_users,name='create_users'),
    url(r'^relative_page/',views.relative_page,name='relative_page'),
    url(r'^register_page/',views.register_page,name='register_page'),
    url(r'^user_login/',views.user_login,name='user_login'),
]
