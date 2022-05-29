from django.db import models


class Issue(models.Model):
    ACTIVE = "ACTIVE"
    FROZEN = "FROZEN"
    RESOLVED = "RESOLVED"
    ISSUE_STATUSES = [
        (ACTIVE, "Active"),
        (FROZEN, "Frozen"),
        (RESOLVED, "Resolved"),
    ]
    created_by = models.CharField(max_length=150, verbose_name="created by")
    status = models.CharField(choices=ISSUE_STATUSES, max_length=255, default=ACTIVE)
    title = models.CharField(max_length=150, verbose_name="title")
    body = models.TextField(verbose_name="Issue description")
    assignee = models.CharField(max_length=150, verbose_name="assigned to")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="created")
    time_updated = models.DateTimeField(auto_now=True, verbose_name="last updated")
    updated_by = models.CharField(max_length=150, verbose_name="updated by")

    def __str__(self):
        return Issue.title


class Comments:
    created_by = models.CharField(max_length=150, verbose_name="created by")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="created")
    updated_by = models.CharField(max_length=150, verbose_name="updated by")
    time_updated = models.DateTimeField(auto_now=True, verbose_name="last updated")
    body = models.TextField(verbose_name="comment")

    def __str__(self):
        return f"id: {self.pk} | {self.time_create.strftime('%d/%m/%y %H:%M')}"
