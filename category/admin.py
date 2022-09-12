from django.contrib import admin

# Register your models here.
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    
    # Esta propiedad hace que el campo slug se genere automaticamente al agregar un nombre de categoria
    prepopulated_fields= {'slug': ('category_name',)}
    
    list_display= ('category_name', 'slug',)

admin.site.register(Category, CategoryAdmin)