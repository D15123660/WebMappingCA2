from login import views
from django.urls import path

urlpatterns = [
    path('users/', views.login.as_view()),
    path('users/(?P<pk>\d+)/', views.login.as_view(),name='user-detail'),

]
