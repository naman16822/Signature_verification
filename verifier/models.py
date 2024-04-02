from django.db import models

class Signature(models.Model):
    image = models.FileField(upload_to='signatures/')
    verified = models.BooleanField(default=False)
    verified_by = models.CharField(max_length=100, blank=True, null=True)
    verification_date = models.DateTimeField(auto_now_add=True)
