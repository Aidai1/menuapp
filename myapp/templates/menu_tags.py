# menu_app/templatetags/menu_tags.py
from django import template
from myapp.models import Menu

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    menu = Menu.objects.get(name=menu_name)
    return menu
