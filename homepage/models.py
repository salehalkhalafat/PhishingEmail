from django.db import models

class EmailList(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)  # Adjust max_length as necessary
    body = models.TextField()

    def __str__(self):
        return f"{self.email} - {self.subject}"
    

