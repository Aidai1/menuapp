# menu_app/admin.py
from django.contrib import admin
from .models import Menu, MenuItem

admin.site.register(Menu)
admin.site.register(MenuItem)
