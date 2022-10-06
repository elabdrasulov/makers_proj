from django.urls import path
from .views import *

urlpatterns = [
    path('groups/create/', GroupCreateAPIView.as_view()),
    path('groups/listing/', GroupListAPIView.as_view()),
    path('groups/update/<int:pk>/', GroupUpdateAPIView.as_view()),
    path('groups/delete/<int:pk>/', GroupDeleteAPIView.as_view()),
]