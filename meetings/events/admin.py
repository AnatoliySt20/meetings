from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Event._meta.fields]

    class Meta:
        model = Event

admin.site.register(Event, EventAdmin)
