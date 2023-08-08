from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    caption = models.TextField(max_length=200, blank=True, null=True)
    done = models.BooleanField(default=False)
    created_on = models.DateTimeField(("Craeted on"), default=timezone.now)
    
    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['-id']


class SharedTask(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    tasks = models.ManyToManyField(Task,related_name="task", symmetrical=False)
    users = models.ManyToManyField(User,blank=True, related_name="sharred", symmetrical=False)
    created_on = models.DateTimeField(("Craeted on"), default=timezone.now)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['-id']