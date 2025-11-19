from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import authenticate
from .models import User
from .serializers import RegisterSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def register(request):
    data = request.data
    serializer = RegisterSerializer(data=data)
    if not serializer.is_valid():
        return Response({'message':'Something is missing or invalid','errors':serializer.errors,'success':False}, status=status.HTTP_400_BAD_REQUEST)

    email = data.get('email')
    if User.objects.filter(email=email).exists():
        return Response({'message':'User already exists','success':False}, status=status.HTTP_400_BAD_REQUEST)

    user = serializer.save()
    user_data = UserSerializer(user).data
    return Response({'message':'Account created','user': user_data,'success':True}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login(request):
    data = request.data
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')

    if not email or not password or not role:
        return Response({'message':'Email or password is missing','success':False}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, username=email, password=password)
    if user is None:
        return Response({'message':'User not found or incorrect credentials','success':False}, status=status.HTTP_400_BAD_REQUEST)

    if user.role != role:
        return Response({'message':'Incorrect role selected','success':False}, status=status.HTTP_400_BAD_REQUEST)

    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    user_data = UserSerializer(user).data

    response = Response({'message':f'Welcome back {user.fullname}','user': user_data,'success':True}, status=status.HTTP_200_OK)
    # Set cookie named 'token' for frontend parity
    response.set_cookie('token', access_token, httponly=True, samesite='Lax')
    return response


@api_view(['POST'])
def logout(request):
    response = Response({'message':'Logged out successfully','success':True}, status=status.HTTP_200_OK)
    response.delete_cookie('token')
    return response
