from django.urls import path
from . import views

urlpatterns = [
    path('user-list/', views.user_view,name='user_view'),
    path('keyword-list/',views.keyword_view,name='keyword_view'),
]
