# myapp/urls.py

from django.urls import path
from .views import user_login, protected_view, user_logout
from .views import front_page
urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('protected/', protected_view, name='protected_view'),
    path('logout/', user_logout, name='user_logout'),
    path('', front_page, name='front_page'),
]
