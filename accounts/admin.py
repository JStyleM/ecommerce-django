from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Account

class AccountAdmin(UserAdmin):
    
    # Forma en como se muestra la lista de usuarios en el admin de django
    list_display= (
        'email', 
        'username', 
        'first_name', 
        'last_name', 
        'last_login', 
        'date_joined', 
        'is_active'
    )
    
    # atributos que tiene link al detalle del usuario
    list_display_links = ('email', 'first_name', 'last_name',)
    # Campos de solo lectura en el detalle de usuario
    readonly_fields = ('last_login', 'date_joined',)
    # Como aparecen ordenados en la lista de usuarios del admin
    ordering = ('-date_joined',)
    
    filter_horizontal= ()
    list_filter= ()
    fieldsets = ()
    

admin.site.register(Account, AccountAdmin)


