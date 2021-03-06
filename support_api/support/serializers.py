from django.contrib.auth.models import User
from rest_framework.relations import PrimaryKeyRelatedField

from support.models import Issue, Comments
from rest_framework import serializers


class IssueSerializer(serializers.ModelSerializer):
    assignee = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    created_by = serializers.CharField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = Issue
        fields = "__all__"
        ordering = ["-id"]


class IssueStatusSerializer(serializers.ModelSerializer):
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Issue
        fields = ['assignee', 'status', "updated_by"]


class CommentSerializer(serializers.ModelSerializer):
    issue = serializers.CharField(read_only=True)
    created_by = serializers.CharField(read_only=True)

    class Meta:
        model = Comments
        fields = "__all__"
