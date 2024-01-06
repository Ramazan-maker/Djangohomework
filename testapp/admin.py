from django.contrib import admin

from .models import AdvUser, Machine, Spare, SMS, Task

admin.site.register(AdvUser)
admin.site.register(Machine)
admin.site.register(Spare)

#homework 13
admin.site.register(SMS)

#homwork_14
admin.site.register(Task)
