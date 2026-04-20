from django.db import models
from django.conf import settings

class DailyReport(models.Model):
    """
    Model representing a synchronized daily report from remote team members.
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    is_synced = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report by {self.author.username} at {self.created_at.strftime('%Y-%m-%d')}"