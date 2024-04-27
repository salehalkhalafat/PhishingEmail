from django.db import models


class EMAILS(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    isfishing = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email} - {self.subject}"
