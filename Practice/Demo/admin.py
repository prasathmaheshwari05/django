# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from.models import Dishes,Chef

# Register your models here.
class dishadmin(admin.ModelAdmin):
    list_display=('name','rating')
    list_filter=['rating']
admin.site.register(Dishes,dishadmin)
admin.site.register(Chef)
