from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated

from knox.auth import AuthToken
from .serializers import UserSerializer

class LoginUserView(APIView):
      def post(self, request):
            serializer = AuthTokenSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            _, token = AuthToken.objects.create(user)
            return Response({'user_info':{'username':user.username, 
                                          'email':user.email}, 'token': token})

class UserProfileView(APIView):
      permission_classes = [IsAuthenticated]
      def get(self, request):
            user=request.user
            return Response({
                        'user_info':{'username':user.username, 
                                    'email':user.email
                              },
                  })
      
class RegisterUserView(APIView):
    def post(self, request):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                  user = serializer.save()
                  _, token = AuthToken.objects.create(user)
                  return Response({'user_info':{
                                        'username':user.username, 
                                        'email':user.email
                                        },
                            'token': token})
            return Response({'error':'check your credentials.'}, status=400)