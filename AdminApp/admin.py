from django.contrib import admin
from AdminApp.models import Category,Gym

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","cat_name")

class GymAdmin(admin.ModelAdmin):
    list_display=("id","service_name","price","description","imageurl","category")


admin.site.register(Category,CategoryAdmin)
admin.site.register(Gym,GymAdmin)
    