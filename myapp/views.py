# menu_app/views.py
from django.shortcuts import render, get_object_or_404
from .models import Menu, MenuItem
from django.shortcuts import redirect



def myapp_home(request):
    return render(request, 'myapp/templates/home.html')


def template_view(request):
    return render(request, 'myapp/templates/menu_template.html')


def draw_menu(request, menu_name):
    if request.method == 'POST':
        selected_menu_item_id = request.POST.get('menu_item_id')
        menu_item = MenuItem.objects.get(pk=selected_menu_item_id)
        return redirect(menu_item.url)
    else:
        menu = get_object_or_404(Menu, name=menu_name)
        current_url = request.path_info
        for item in menu.cached_items:
            if item.url == current_url:
                item.active = True
            else:
                item.active = False
        return render(request, 'myapp/templates/menu_template.html', {'menu': menu})
