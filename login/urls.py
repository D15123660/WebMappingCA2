from rest_framework import routers
from login import views
from django.urls import path

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('users/', views.login.as_view()),
    path('users/(?P<pk>\d+)/', views.login.as_view(), name='user-detail'),

]
