from django.shortcuts import render
from rest_framework import generics, viewsets
from support.models import Issue, Comments
from support.serializers import IssueSerializer


class IssueAPIView(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
