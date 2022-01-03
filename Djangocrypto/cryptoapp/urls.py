from django.urls import path
from . import views
urlpatterns = [
    path('/home1',views.index, name="home1"),
    path('/fav',views.favorite,name='fav'),
    path('login',views.user_login,name='login'),
    path('',views.register_request,name='registeration'),
]
