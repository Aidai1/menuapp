# menu_app/urls.py
from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('draw_menu/<str:menu_name>/',views.draw_menu, name='draw_menu'),
    path('template/', views.template_view, name='template'),
    path('', views.myapp_home, name='myapp_home'),
]
