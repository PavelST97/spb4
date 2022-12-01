from django.contrib import admin
from . import models


class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'datetime', 'status']
    list_display_links = ['title']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'datetime']
    list_display_links = ['title']


class PersonAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_support']
    list_display_links = ['user']


admin.site.register(models.Ticket, TicketAdmin)
admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Comment, CommentAdmin)
