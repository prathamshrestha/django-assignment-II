from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import login_view, profile, logout_view, signup_view
from .crud_views import Create,List


urlpatterns=[
    path('login/',login_view.as_view(),name='login'),
    path('profile/',login_required(profile.as_view()),name='profile'),
    path('logout/',logout_view.as_view(),name='logout'),
    path('signup/',signup_view.as_view(),name='signup'),
    path('create/',Create.as_view(),name='create'),
    path('list/',List.as_view(),name='List'),

]