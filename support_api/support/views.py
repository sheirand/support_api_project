from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.viewsets import GenericViewSet

from support.models import Issue, Comments
from support.serializers import IssueSerializer, IssueStatusSerializer
from rest_framework.views import APIView, Response



class CreateListRetrieveViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'list', 'retrieve']:
            serializer_class = IssueSerializer
        else:
            serializer_class = IssueStatusSerializer

        return serializer_class

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
