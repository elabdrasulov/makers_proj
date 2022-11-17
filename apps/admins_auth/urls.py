from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import *

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
]