from django.urls import path
from .views import *

urlpatterns = [
    path('staffs/create/', StaffCreateAPIView.as_view()),
    path('staffs/<int:pk>/', StaffDetailAPIView.as_view()),
    path('staffs/', StaffListAPIView.as_view()),
    path('staffs/update/<int:pk>/', StaffUpdateAPIView.as_view()),
    path('staffs/delete/<int:pk>/', StaffDeleteAPIView.as_view()), 
    path('staffs/ready_to_be_mentor/', ready_to_be_mentor),
    path('staffs/free_mentor/', free_mentor),
]