"""support_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from support.views import IssueViewSet, CommentsViewSet
from rest_framework.routers import DefaultRouter

router_issue = DefaultRouter()
router_comment = DefaultRouter()
router_issue.register('issue', IssueViewSet, basename='Issue')
router_comment.register('comment', CommentsViewSet, basename='comment')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router_issue.urls)),
    path('', include('rest_framework.urls')),
    path('api/v1/issue/<int:issue_id>/', include(router_comment.urls)),
]
