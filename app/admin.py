from django.contrib.admin import site
from .models import *

site.register(Task)
site.register(SharredTask)
