from django.db import models

class Register(models.Model):

    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    email = models.EmailField()
    telephone = models.IntegerField()
    hobbies = models.TextField()

    email_verified = models.BooleanField(default=False)
    telephone_verified = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Register'