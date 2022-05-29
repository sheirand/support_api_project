from support.models import Issue, Comments
from rest_framework import serializers


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"

