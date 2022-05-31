from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from support.models import Issue, Comments
from support.serializers import IssueSerializer, IssueStatusSerializer, CommentSerializer
from support.permissions import IsOwnerOrStaff, IsStaff


class IssueViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if self.request.user.is_staff:
            if not pk:
                return Issue.objects.all()
            else:
                return Issue.objects.filter(pk=pk)
        else:
            if not pk:
                return Issue.objects.filter(created_by=self.request.user)
            else:
                return Issue.objects.filter(created_by=self.request.user, pk=pk)

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
        elif self.action in ['update', 'destroy',
                             'partial_update',
                             'perform_update']:
            permission_classes = [IsStaff, IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class CommentsViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    permission_classes = [IsOwnerOrStaff]
    serializer_class = CommentSerializer

    def get_queryset(self):
        issue_id = self.kwargs.get('issue_id')
        pk = self.kwargs.get('pk')
        if not pk:
            return Comments.objects.filter(issue_id=issue_id)
        else:
            return Comments.objects.filter(issue_id=issue_id, pk=pk)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, issue_id=self.kwargs.get('issue_id'))
