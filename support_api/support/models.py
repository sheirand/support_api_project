from django.db import models
from django.contrib.auth.models import User


class Issue(models.Model):
    ACTIVE = "ACTIVE"
    FROZEN = "FROZEN"
    RESOLVED = "RESOLVED"
    ISSUE_STATUSES = [
        (ACTIVE, "Active"),
        (FROZEN, "Frozen"),
        (RESOLVED, "Resolved"),
    ]
    STAFF_LIST = [(str(staff), str(staff)) for staff in User.objects.filter(is_staff=True)]

    created_by = models.ForeignKey(User, verbose_name="created by", on_delete=models.CASCADE, related_name="Issue_created_by")
    status = models.CharField(choices=ISSUE_STATUSES, max_length=255, default=ACTIVE)
    title = models.CharField(max_length=150, verbose_name="title")
    body = models.TextField(verbose_name="Issue description")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="created")
    time_updated = models.DateTimeField(auto_now=True, verbose_name="last updated")
    updated_by = models.ForeignKey(User, related_name="Issue_updated_by",
                                   on_delete=models.CASCADE, null=True)
    assignee = models.CharField(choices=STAFF_LIST, max_length=150, null=True)

    class Meta:
        ordering = ['-time_created']

    def __str__(self):
        return self.title


class Comments(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, verbose_name="created by", on_delete=models.PROTECT)
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="created")
    body = models.TextField(verbose_name="comment")

    class Meta:
        verbose_name_plural = "Comments"
        ordering = ['-time_created']

    def __str__(self):
        return f"id: {self.pk} | {self.time_created.strftime('%d/%m/%y %H:%M')}"


