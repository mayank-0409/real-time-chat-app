from django.urls import path
from a_user.views import *

urlpatterns = [
    path('', profile_view, name='profile'),
]