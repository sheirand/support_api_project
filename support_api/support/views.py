from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from support.models import Issue, Comments
from support.serializers import IssueSerializer, IssueStatusSerializer
from rest_framework.views import APIView, Response
from support.permissions import IsOwnerOrStaff, IsStaff


class CreateListRetrieveViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.request.user.is_staff:
            pk = self.kwargs.get("pk")

            if not pk:
                return Issue.objects.all()

            return Issue.objects.filter(pk=pk)
        else:
            return Issue.objects.none()

    def get_serializer_class(self):
        if self.action in ['update', 'partially_update',
                           'destroy']:
            serializer_class = IssueStatusSerializer
        else:
            serializer_class = IssueSerializer

        return serializer_class

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'retrieve':
            permission_classes = [IsOwnerOrStaff]
        elif self.action in ['update', 'list', 'create'
                             'partial_update', 'destroy']:
            permission_classes = [AllowAny]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
