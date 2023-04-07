from django.db import models
from django.contrib.auth.models import AbstractUser

# from django.urls import reverse

GENDER = (('man', 'Man'), ('woman', 'Woman'))


class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=250,
        unique=True,
    )
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True)

    def __str__(self):
        return self.email
    
    # def get_absolute_url(self):
    #     """
    #     this way we can redirect user to profile inside template
    #     using get absolute url function
    #     """
    #     return reverse('authenticate:user-profile', args=[str(self.username)])
    