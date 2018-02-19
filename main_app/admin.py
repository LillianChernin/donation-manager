from django.contrib import admin
from .models import ReliefEffort
from .models import ItemRequest

# Register your models here.
admin.site.register(ReliefEffort)
admin.site.register(ItemRequest)
