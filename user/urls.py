from django.urls import path
from .views import Register,Login,Logout
app_name = 'user'
urlpatterns = [
    path('user/thanks/', Register, name="join"),
    path('login/', Login, name="login"),
    path('logout/', Logout, name="logout"),
]