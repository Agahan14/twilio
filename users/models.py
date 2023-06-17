from django.db import models


class PhoneVerification(models.Model):
    phone_number = models.CharField(max_length=20)
    verification_code = models.CharField(max_length=6)
    is_verified = models.BooleanField(default=False)


class Banner(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title