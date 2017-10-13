from django.contrib  import admin
from .models import *

class MemberInline(admin.TabularInline):
    model = Member
    #extra = 0

class EventAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Event._meta.fields]
    inlines = [MemberInline]
    class Meta:
        model = Event
admin.site.register(Event, EventAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Member._meta.fields]
    class Meta:
        model = Member
admin.site.register(Member, MemberAdmin)