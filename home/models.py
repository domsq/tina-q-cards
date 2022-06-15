from django.db import models


class WelcomeMessage(models.Model):
    """Schema for the WelcomeMessage model"""

    class Meta:
        verbose_name_plural = 'WelcomeMessage'

    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title
