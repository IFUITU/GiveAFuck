from django.urls import path
from . import views
import hashlib
# import random ,string
app_name = "main"
# hashlib.sha1(int(id)).hexdigest() 

urlpatterns = [
    path("", views.index, name="index"),
    path('det4|1+_+/<int:id>/', views.detail, name="detail"),
    path('category/<int:id>/', views.by_category, name='by-category'),
    path('top-100/', views.top_100, name="top-100"),
    path('1ik3-dwnld/<int:pk>/<str:type>/', views.Like.as_view(), name="Like"), #as_view() you can send values via this!
    path('Bonuses--/', views.bonuses, name='bonuses'),
    path('hmac=o"xshamadi/5onu5-detail/<int:id>*2/', views.Bonus_Detail.as_view(), name="bonus"),
    path('search/',views.search, name="search"),
]