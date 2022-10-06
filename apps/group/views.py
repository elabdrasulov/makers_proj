from .serializers import GroupSerializer
from .models import Group
from rest_framework.generics import *
from rest_framework.permissions import IsAdminUser
 
class GroupCreateAPIView(CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminUser,]

class GroupListAPIView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminUser,]

class GroupDetailAPIView(RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminUser,]

class GroupUpdateAPIView(UpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminUser,]

class GroupDeleteAPIView(DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminUser,]

