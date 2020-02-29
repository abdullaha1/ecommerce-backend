from django.shortcuts import render
from .models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializer import UserSerializer
# Create your views here.


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
