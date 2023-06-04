from django.db import models
from django.contrib.auth.models import AbstractUser

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
        return self.username

    class Meta:
        ordering = ['-id']
        # (-) yoki (+) modellar ro'yahti qanday tuzish keark ekanligiga ta'sir qiladi

class Profile(models.Model):
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"
    user = models.OneToOneField(CustomUser(), on_delete=models.CASCADE)
    profile_photo = models.ImageField(default="profile/profile.jpg", upload_to="profile")
    bio = models.CharField(max_length=100, null=True, blank=True, default="")
    verifyed = models.BooleanField(default=False)
    def __str__(self):
        return f"id: {self.id}, {self.user}"