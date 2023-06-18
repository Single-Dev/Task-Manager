from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    caption = models.TextField(max_length=200, blank=True, null=True)
    done = models.BooleanField(default=False)
    # FIRE = 'Fire'
    # WARNING = 'Warning'
    # mark_symbols = [
    #     (FIRE, "🔥"),
    #     (WARNING, "⚠️")
    # ]
    # mark = models.CharField(max_length=15, choices=mark_symbols)
    created_on = models.DateTimeField(("Craeted oN"), default=timezone.now)
    reminder = models.DateField(('Reminder'), blank=True, null=True)
    # attachment = models.FileField(upload_to='base/attachments', blank=True, null=True)
    
    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['-id']