# menu_tags.py

from django import template
from .models import MenuItem

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(parent__isnull=True)
    return {
        'menu_name': menu_name,
        'menu_items': menu_items
    }
