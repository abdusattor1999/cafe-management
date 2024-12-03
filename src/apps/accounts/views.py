from rest_framework_simplejwt.views import TokenViewBase
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.urls import reverse
from .models import User
from .serializers import PublicUserSerializer, LoginSerializer, SignupSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action

class RegisterView(APIView):
    serializer_class = SignupSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active = False  # User is inactive until verified
            user.save()

            # Send verification email
            # verification_url = request.build_absolute_uri(
            #     reverse('accounts.verify', kwargs={'token': user.verification_token})
            # )
            # send_mail(
            #     subject='Verify your Coffee Shop account',
            #     message=f'Click the link to verify your account: {verification_url}',
            #     from_email=None,
            #     recipient_list=[user.email],
            # )
            return Response({'message': 'Registration successful. Check your email for verification.{}'.format(user.verification_token)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        token = request.data.get('token')
        user = User.objects.filter(verification_token=token, is_verified=False).first()
        if user:
            user.verify()
            return Response({'message': 'Verification successful'}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid verification token'}, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(TokenViewBase):
    serializer_class = LoginSerializer


class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = PublicUserSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return Response({'message': 'Registration endpoint is not here'}, status=status.HTTP_404_NOT_FOUND)
    
    def retrieve(self, request, *args, **kwargs):
        user = self.queryset.get(id=kwargs['pk'])
        data = self.get_serializer(user).data
        return Response(data)
    
    def partial_update(self, request, *args, **kwargs):
        user = self.queryset.get(id=kwargs['pk'])
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, methods=['POST'], url_path='me')
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
    

