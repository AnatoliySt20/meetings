from django.contrib  import admin
from .models import *



class MyUserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MyUser._meta.fields]
    class Meta:
        model = MyUser
admin.site.register(MyUser, MyUserAdmin)

