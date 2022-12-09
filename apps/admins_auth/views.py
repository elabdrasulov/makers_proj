from rest_framework import serializers, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError as exc:
            self.fail('bad_token')

class LogoutAPIView(GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        serializers = self.serializer_class(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"msg":"You successfully logged out"}, 
            status=status.HTTP_204_NO_CONTENT
        )


from django.contrib.admin.models import LogEntry
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
import json

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry
        fields = '__all__'
    
    def to_representation(self, instance:LogEntry):
        rep = super().to_representation(instance)
        a=json.loads(rep['change_message'])
        print(a, '!!!!!!!!!!!!!!!11')

    def to_representation(self, instance:LogEntry):
        rep = super().to_representation(instance)
        print(rep)
        # a=json.loads(rep['change_message'])
        rep['change_message'] = json.loads(rep['change_message'])
        
        return rep


class Logs(APIView):
    def get(self, request):
        return Response(LogSerializer(LogEntry.objects.all(), many=True).data)