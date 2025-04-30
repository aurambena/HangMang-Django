from django.contrib import admin
from .models import  PlayerStats
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

# Register your models here.
admin.site.unregister(User)
class CustomUserAdmin(DefaultUserAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active')

admin.site.register(User, CustomUserAdmin)

admin.site.register(PlayerStats)
class UserStats(admin.ModelAdmin):
    model = PlayerStats
    list_display = ('user', 'victories', 'games_played', 'pk')


