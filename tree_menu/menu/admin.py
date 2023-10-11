from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import MenuItem


class MenuItemAdmin(MPTTModelAdmin):
    list_display = ("name", "url")
    # Другие настройки админки


admin.site.register(MenuItem, MenuItemAdmin)
