from django.utils.functional import cached_property
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    @cached_property
    def cached_items(self):
        return list(self.items.all())

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title
